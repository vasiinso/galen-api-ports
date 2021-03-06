/****************************************************************************
 * Copyright 2015 Valerio Morsella                                          *
 *                                                                          *
 * Licensed under the Apache License, Version 2.0 (the "License");          *
 * you may not use this file except in compliance with the License.         *
 * You may obtain a copy of the License at                                  *
 *                                                                          *
 *    http://www.apache.org/licenses/LICENSE-2.0                            *
 *                                                                          *
 * Unless required by applicable law or agreed to in writing, software      *
 * distributed under the License is distributed on an "AS IS" BASIS,        *
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. *
 * See the License for the specific language governing permissions and      *
 * limitations under the License.                                           *
 ****************************************************************************/

package galen.api.server;

import galen.api.server.thrift.*;
import galen.api.server.thrift.Response;
import galen.api.server.utils.StringUtils;
import net.mindengine.galen.api.Galen;
import net.mindengine.galen.reports.GalenTestInfo;
import net.mindengine.galen.reports.HtmlReportBuilder;
import net.mindengine.galen.reports.TestReport;
import net.mindengine.galen.reports.model.LayoutReport;
import org.apache.thrift.TException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriverException;
import org.openqa.selenium.remote.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.*;

import static com.google.common.collect.Maps.newHashMap;
import static galen.api.server.GsonUtils.getGson;
import static galen.api.server.utils.TestReportUtils.buildTestReportFromReportTree;
import static java.lang.String.format;
import static org.openqa.selenium.remote.ErrorCodes.SESSION_NOT_CREATED;
import static org.openqa.selenium.remote.ErrorCodes.SUCCESS;

public class GalenCommandExecutor implements GalenApiRemoteService.Iface {
    private Logger log = LoggerFactory.getLogger(GalenApiServer.class);

    private String remoteServerAddress;

    @Override
    public void initialize(String remoteServerAddress) throws TException {
        this.remoteServerAddress = remoteServerAddress;
    }

    /**
     * Executes the command received over the Thrift interface inside an instance of RemoteWebDriver.
     * @param sessionId WebDriver SessionId.
     * @param commandName Command name.
     * @param params Command params.
     * @return an instance of {@link org.openqa.selenium.remote.Response}
     * @throws TException
     */
    @Override
    public Response execute(String sessionId, String commandName, String params) throws TException {
        Map<String, Object> paramsAsMap = fromJsonToStringObjectMap(params);
        if (commandName.equals(DriverCommand.NEW_SESSION)) {
            try {
                log.info("Setting up new WebDriver session");
                HashMap<String, Object> hashMap = extractDesiredCapabilities(paramsAsMap);
                WebDriver driver = new RemoteWebDriver(new URL(remoteServerAddress), new DesiredCapabilities(hashMap));
                DriversPool.get().set(driver);
                return createSessionInitSuccessResponse(driver);
            } catch (MalformedURLException e) {
                log.error("Provided URL is malformed " + remoteServerAddress);
                return createSessionInitFailureResponse("Provided URL is malformed " + remoteServerAddress);
            } catch (UnreachableBrowserException e) {
                log.error("Could not reach browser at URL " + remoteServerAddress + " check remote server is running.");
                return createSessionInitFailureResponse("Could not reach browser at URL " + remoteServerAddress +
                        " check remote server is running.");
            } catch (WebDriverException e) {
                throw new RemoteWebDriverException(e.getMessage());
            }
        }
        Command driverCommand = new Command(new SessionId(sessionId), handleCommandNameExceptions(commandName), paramsAsMap);
        try {
            log.info(format("Executing command %s for sessionId %s", commandName, sessionId));
            WebDriver driver = DriversPool.get().getBySessionId(sessionId);
            org.openqa.selenium.remote.Response response = null;
            if (driver instanceof RemoteWebDriver) {
                response = ((RemoteWebDriver) driver).getCommandExecutor().execute(driverCommand);
            }
            if (response == null) {
                return null;
            } else {
                if (commandName.equals(DriverCommand.QUIT)) {
                    DriversPool.get().removeDriverBySessionId(sessionId);
                }
                ThriftValueWrapper valueWrapper = new ThriftValueWrapper(response.getValue());
                return new Response(valueWrapper.getValue(), valueWrapper.getContainedValues(), response.getSessionId(),
                        response.getStatus(), response.getState());
            }
        } catch (IOException ioe) {
            log.error(format("IOException while executing command %s: %s", commandName, ioe.toString()));
        } catch (WebDriverException wex) {
            log.error(format("WebDriverException while executing command %s: + %s", commandName, wex.toString()));
            throw new RemoteWebDriverException(wex.getMessage());
        }
        return null;
    }

    /**
     * Register test by name,
     * @param testName A unique name for the test.
     */
    @Override
    public void register_test(String testName) {
        GalenReportsContainer.get().registerTest(testName);
    }

    /**
     * Main method of the API. Validates current page layout against the provided specs.
     * @param driverSessionId WebDriver SessionId to be used to scan the page under test.
     * @param specs .specs file containing the Galen specification of the page under test.
     * @param includedTags Tags to be included in the check.
     * @param excludedTags Tags to be excluded from the check.
     * @return A unique id of the layoutReport generated after the check.
     * @throws SpecNotFoundException
     */
    @Override
    public LayoutCheckReport check_layout(String driverSessionId, String specs, List<String> includedTags, List<String> excludedTags)
            throws SpecNotFoundException {
        LayoutReport layoutReport = new LayoutReport();
        log.info(format("Executing check_layout for spec " + specs + " with driver " + driverSessionId));
        WebDriver driver = DriversPool.get().getBySessionId(driverSessionId);
        String reportId = null;
        try {
            layoutReport = Galen.checkLayout(driver, specs, includedTags, excludedTags, new Properties(),
                    null);
            reportId = StringUtils.generateUniqueString();
            GalenReportsContainer.get().storeLayoutReport(reportId, layoutReport);
        } catch (FileNotFoundException e) {
            log.error("Could not find spec file " + specs);
            throw new SpecNotFoundException(e.getMessage());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return new LayoutCheckReport(reportId, layoutReport.errors(), layoutReport.warnings());
    }

    /**
     * Appends the generated test report to the main report.
     * @param testName Name of the test to be run. This is the text that is displayed in the test report overview.
     * @param reportTree Structure passed over the Thrift interface to hold information about the report structure that
     *                   is built in the client side.
     * @throws TException
     */
    @Override
    public void append(String testName, ReportTree reportTree) throws TException {
        GalenReportsContainer galenReportsContainer = GalenReportsContainer.get();
        galenReportsContainer.updateEndTime(testName);

        TestReport testReport = new TestReport();
        buildTestReportFromReportTree(testReport, reportTree, reportTree.getRoot_id());
        galenReportsContainer.getTestWithName(testName).setReport(testReport);
    }

    /**
     * Generates the Galen report inside the provided folder path.
     * @param reportFolderPath target folder where to store the generated report.
     * @throws TException
     */
    @Override
    public void generate_report(String reportFolderPath) throws TException {
        List<GalenTestInfo> tests = GalenReportsContainer.get().getAllTests();
        try {
            new HtmlReportBuilder().build(tests, reportFolderPath);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Returns the number of active WebDriver sessions.
     */
    @Override
    public int active_drivers() throws TException {
        return DriversPool.get().activeDrivers();
    }

    /**
     * Shuts down the service.
     */
    @Override
    public void shut_service() throws TException {
        log.info("Shutting down Galen API service.");
        System.exit(1);
    }

    /**
     * As it turns out that Java and Python implementations differs in the command names, this method is to align naming
     * to conventions used in Java {@link org.openqa.selenium.remote.RemoteWebDriver}
     */
    private String handleCommandNameExceptions(String name) {
        if (name.equals("windowMaximize")) {
            name = DriverCommand.MAXIMIZE_WINDOW;
        } else if (name.equals("setTimeouts")) {
            name = DriverCommand.SET_TIMEOUT;
        }
        return name;
    }

    /**
     * Transform a json String into a map of Object indexed by a String value.
     * This is needed to feed Command and DesideredCapabilities constructor.
     */
    private Map<String, Object> fromJsonToStringObjectMap(String params) {
        return getGson().<Map<String, Object>>fromJson(params, Object.class);
    }

    /**
     * Packages a successful session setup response which can be sent across the Thrift interface.
     */
    private Response createSessionInitSuccessResponse(WebDriver driver) {
        Response response = new Response();
        response.setStatus(SUCCESS);
        RemoteWebDriver remoteDriver = (RemoteWebDriver) driver;
        ThriftValueWrapper wrappedValue = new ThriftValueWrapper(remoteDriver.getCapabilities().asMap());
        response.setResponse_value(wrappedValue.getValue());
        response.setContained_values(wrappedValue.getContainedValues());
        response.setSession_id(remoteDriver.getSessionId().toString());
        response.setState(new ErrorCodes().toState(SUCCESS));
        return response;
    }

    /**
     * Packages a failing session setup response which can be sent across the Thrift interface.
     */
    private Response createSessionInitFailureResponse(String reason) {
        Response response = new Response();
        response.setStatus(SESSION_NOT_CREATED);
        response.setState(new ErrorCodes().toState(SESSION_NOT_CREATED));
        ResponseValue value = new ResponseValue();
        Value valueType = new Value();
        valueType.setString_value(reason);
        value.setValue(valueType);
        response.setResponse_value(value);
        return response;
    }

    /**
     * Extract desired capabilities from json document as received over Thrift interface into a HashMap
     * where the key set is the names of the capabilities.
     */
    private static HashMap<String, Object> extractDesiredCapabilities(Map<String, Object> paramsAsMap) {
        Map<String, Object> desiredCapabilities;
        if (paramsAsMap.containsKey("desiredCapabilities")) {
            desiredCapabilities = (Map<String, Object>) paramsAsMap.get("desiredCapabilities");
        } else {
            throw new IllegalStateException("New session does not contain desired capabilities.");
        }
        HashMap<String, Object> hashMap = newHashMap();
        Set<String> keySet = desiredCapabilities.keySet();
        for (String key : keySet) {
            hashMap.put(key, desiredCapabilities.get(key));
        }
        return hashMap;
    }
}
