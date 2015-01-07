import json
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.webdriver import WebDriver

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import RemoteCommandExecutor


class GalenWebDriver(WebDriver):
    def __init__(self, remote_url='http://127.0.0.1:4444/wd/hub', desired_capabilities=None, browser_profile=None,
                 proxy=None, keep_alive=False):
        self.thrift = ThriftFacade()
        desired_caps_json = None
        if desired_capabilities:
            desired_caps_json = json.dumps(desired_capabilities)
        self.thrift.client.initialize(remote_url, desired_caps_json)
        WebDriver.__init__(self, GalenRemoteConnection(remote_url, self.thrift.client), desired_capabilities,
                           browser_profile, proxy, keep_alive)

    def quit(self):
        super(GalenWebDriver, self).quit()
        self.thrift.close_connection()


class ThriftFacade():
    def __init__(self):
        try:
            self.transport = TSocket.TSocket('localhost', 9091)
            self.transport = TTransport.TBufferedTransport(self.transport)
            protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
            self.client = RemoteCommandExecutor.Client(protocol)
            self.transport.open()
        except Thrift.TException, tx:
            print '%s' % (tx.message)

    def close_connection(self):
        self.transport.close()


class GalenRemoteConnection(RemoteConnection):
    def __init__(self, remote_server_addr, thrift_client, keep_alive=False):
        super(GalenRemoteConnection, self).__init__(remote_server_addr, keep_alive)
        self.thrift_client = thrift_client

    def execute(self, command, params):
        command_info = self._commands[command]
        assert command_info is not None, 'Unrecognised command %s' % command
        data = json.dumps(params)

        response = self.thrift_client.execute(command, data)
        return {'status': response.status, 'sessionId': response.session_id, 'state': response.state,
                'value': response.value.string_cap}


CHROME = {
    "browserName": "chrome",
    "version": "",
    "platform": "ANY"
}

driver = GalenWebDriver("http://localhost:4444/wd/hub", desired_capabilities=CHROME)
driver.get("http://www.google.it")
driver.quit()
