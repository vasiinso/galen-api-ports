#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def initialize(self, remote_server_addr):
    """
    Parameters:
     - remote_server_addr
    """
    pass

  def execute(self, session_id, command, params):
    """
    Parameters:
     - session_id
     - command
     - params
    """
    pass

  def check_layout(self, test_name, webdriver_session_id, specs, included_tags, excluded_tags):
    """
    Parameters:
     - test_name
     - webdriver_session_id
     - specs
     - included_tags
     - excluded_tags
    """
    pass

  def generate_report(self, report_folder_path):
    """
    Parameters:
     - report_folder_path
    """
    pass

  def active_drivers(self):
    pass

  def shut_service(self):
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def initialize(self, remote_server_addr):
    """
    Parameters:
     - remote_server_addr
    """
    self.send_initialize(remote_server_addr)
    self.recv_initialize()

  def send_initialize(self, remote_server_addr):
    self._oprot.writeMessageBegin('initialize', TMessageType.CALL, self._seqid)
    args = initialize_args()
    args.remote_server_addr = remote_server_addr
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_initialize(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = initialize_result()
    result.read(iprot)
    iprot.readMessageEnd()
    return

  def execute(self, session_id, command, params):
    """
    Parameters:
     - session_id
     - command
     - params
    """
    self.send_execute(session_id, command, params)
    return self.recv_execute()

  def send_execute(self, session_id, command, params):
    self._oprot.writeMessageBegin('execute', TMessageType.CALL, self._seqid)
    args = execute_args()
    args.session_id = session_id
    args.command = command
    args.params = params
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_execute(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = execute_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.exc is not None:
      raise result.exc
    raise TApplicationException(TApplicationException.MISSING_RESULT, "execute failed: unknown result");

  def check_layout(self, test_name, webdriver_session_id, specs, included_tags, excluded_tags):
    """
    Parameters:
     - test_name
     - webdriver_session_id
     - specs
     - included_tags
     - excluded_tags
    """
    self.send_check_layout(test_name, webdriver_session_id, specs, included_tags, excluded_tags)
    return self.recv_check_layout()

  def send_check_layout(self, test_name, webdriver_session_id, specs, included_tags, excluded_tags):
    self._oprot.writeMessageBegin('check_layout', TMessageType.CALL, self._seqid)
    args = check_layout_args()
    args.test_name = test_name
    args.webdriver_session_id = webdriver_session_id
    args.specs = specs
    args.included_tags = included_tags
    args.excluded_tags = excluded_tags
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_check_layout(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = check_layout_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.exc is not None:
      raise result.exc
    raise TApplicationException(TApplicationException.MISSING_RESULT, "check_layout failed: unknown result");

  def generate_report(self, report_folder_path):
    """
    Parameters:
     - report_folder_path
    """
    self.send_generate_report(report_folder_path)
    self.recv_generate_report()

  def send_generate_report(self, report_folder_path):
    self._oprot.writeMessageBegin('generate_report', TMessageType.CALL, self._seqid)
    args = generate_report_args()
    args.report_folder_path = report_folder_path
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_generate_report(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = generate_report_result()
    result.read(iprot)
    iprot.readMessageEnd()
    return

  def active_drivers(self):
    self.send_active_drivers()
    return self.recv_active_drivers()

  def send_active_drivers(self):
    self._oprot.writeMessageBegin('active_drivers', TMessageType.CALL, self._seqid)
    args = active_drivers_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_active_drivers(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = active_drivers_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "active_drivers failed: unknown result");

  def shut_service(self):
    self.send_shut_service()
    self.recv_shut_service()

  def send_shut_service(self):
    self._oprot.writeMessageBegin('shut_service', TMessageType.CALL, self._seqid)
    args = shut_service_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_shut_service(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = shut_service_result()
    result.read(iprot)
    iprot.readMessageEnd()
    return


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["initialize"] = Processor.process_initialize
    self._processMap["execute"] = Processor.process_execute
    self._processMap["check_layout"] = Processor.process_check_layout
    self._processMap["generate_report"] = Processor.process_generate_report
    self._processMap["active_drivers"] = Processor.process_active_drivers
    self._processMap["shut_service"] = Processor.process_shut_service

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_initialize(self, seqid, iprot, oprot):
    args = initialize_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = initialize_result()
    self._handler.initialize(args.remote_server_addr)
    oprot.writeMessageBegin("initialize", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_execute(self, seqid, iprot, oprot):
    args = execute_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = execute_result()
    try:
      result.success = self._handler.execute(args.session_id, args.command, args.params)
    except RemoteWebDriverException, exc:
      result.exc = exc
    oprot.writeMessageBegin("execute", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_check_layout(self, seqid, iprot, oprot):
    args = check_layout_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = check_layout_result()
    try:
      result.success = self._handler.check_layout(args.test_name, args.webdriver_session_id, args.specs, args.included_tags, args.excluded_tags)
    except SpecNotFoundException, exc:
      result.exc = exc
    oprot.writeMessageBegin("check_layout", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_generate_report(self, seqid, iprot, oprot):
    args = generate_report_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = generate_report_result()
    self._handler.generate_report(args.report_folder_path)
    oprot.writeMessageBegin("generate_report", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_active_drivers(self, seqid, iprot, oprot):
    args = active_drivers_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = active_drivers_result()
    result.success = self._handler.active_drivers()
    oprot.writeMessageBegin("active_drivers", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_shut_service(self, seqid, iprot, oprot):
    args = shut_service_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = shut_service_result()
    self._handler.shut_service()
    oprot.writeMessageBegin("shut_service", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class initialize_args:
  """
  Attributes:
   - remote_server_addr
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'remote_server_addr', None, None, ), # 1
  )

  def __init__(self, remote_server_addr=None,):
    self.remote_server_addr = remote_server_addr

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.remote_server_addr = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('initialize_args')
    if self.remote_server_addr is not None:
      oprot.writeFieldBegin('remote_server_addr', TType.STRING, 1)
      oprot.writeString(self.remote_server_addr)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.remote_server_addr)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class initialize_result:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('initialize_result')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class execute_args:
  """
  Attributes:
   - session_id
   - command
   - params
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'session_id', None, None, ), # 1
    (2, TType.STRING, 'command', None, None, ), # 2
    (3, TType.STRING, 'params', None, None, ), # 3
  )

  def __init__(self, session_id=None, command=None, params=None,):
    self.session_id = session_id
    self.command = command
    self.params = params

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.session_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.command = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.params = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('execute_args')
    if self.session_id is not None:
      oprot.writeFieldBegin('session_id', TType.STRING, 1)
      oprot.writeString(self.session_id)
      oprot.writeFieldEnd()
    if self.command is not None:
      oprot.writeFieldBegin('command', TType.STRING, 2)
      oprot.writeString(self.command)
      oprot.writeFieldEnd()
    if self.params is not None:
      oprot.writeFieldBegin('params', TType.STRING, 3)
      oprot.writeString(self.params)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.session_id)
    value = (value * 31) ^ hash(self.command)
    value = (value * 31) ^ hash(self.params)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class execute_result:
  """
  Attributes:
   - success
   - exc
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Response, Response.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'exc', (RemoteWebDriverException, RemoteWebDriverException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, exc=None,):
    self.success = success
    self.exc = exc

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Response()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.exc = RemoteWebDriverException()
          self.exc.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('execute_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.exc is not None:
      oprot.writeFieldBegin('exc', TType.STRUCT, 1)
      self.exc.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.exc)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class check_layout_args:
  """
  Attributes:
   - test_name
   - webdriver_session_id
   - specs
   - included_tags
   - excluded_tags
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'test_name', None, None, ), # 1
    (2, TType.STRING, 'webdriver_session_id', None, None, ), # 2
    (3, TType.STRING, 'specs', None, None, ), # 3
    (4, TType.LIST, 'included_tags', (TType.STRING,None), None, ), # 4
    (5, TType.LIST, 'excluded_tags', (TType.STRING,None), None, ), # 5
  )

  def __init__(self, test_name=None, webdriver_session_id=None, specs=None, included_tags=None, excluded_tags=None,):
    self.test_name = test_name
    self.webdriver_session_id = webdriver_session_id
    self.specs = specs
    self.included_tags = included_tags
    self.excluded_tags = excluded_tags

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.test_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.webdriver_session_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.specs = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.included_tags = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = iprot.readString();
            self.included_tags.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.excluded_tags = []
          (_etype16, _size13) = iprot.readListBegin()
          for _i17 in xrange(_size13):
            _elem18 = iprot.readString();
            self.excluded_tags.append(_elem18)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('check_layout_args')
    if self.test_name is not None:
      oprot.writeFieldBegin('test_name', TType.STRING, 1)
      oprot.writeString(self.test_name)
      oprot.writeFieldEnd()
    if self.webdriver_session_id is not None:
      oprot.writeFieldBegin('webdriver_session_id', TType.STRING, 2)
      oprot.writeString(self.webdriver_session_id)
      oprot.writeFieldEnd()
    if self.specs is not None:
      oprot.writeFieldBegin('specs', TType.STRING, 3)
      oprot.writeString(self.specs)
      oprot.writeFieldEnd()
    if self.included_tags is not None:
      oprot.writeFieldBegin('included_tags', TType.LIST, 4)
      oprot.writeListBegin(TType.STRING, len(self.included_tags))
      for iter19 in self.included_tags:
        oprot.writeString(iter19)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.excluded_tags is not None:
      oprot.writeFieldBegin('excluded_tags', TType.LIST, 5)
      oprot.writeListBegin(TType.STRING, len(self.excluded_tags))
      for iter20 in self.excluded_tags:
        oprot.writeString(iter20)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.test_name)
    value = (value * 31) ^ hash(self.webdriver_session_id)
    value = (value * 31) ^ hash(self.specs)
    value = (value * 31) ^ hash(self.included_tags)
    value = (value * 31) ^ hash(self.excluded_tags)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class check_layout_result:
  """
  Attributes:
   - success
   - exc
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
    (1, TType.STRUCT, 'exc', (SpecNotFoundException, SpecNotFoundException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, exc=None,):
    self.success = success
    self.exc = exc

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.exc = SpecNotFoundException()
          self.exc.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('check_layout_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    if self.exc is not None:
      oprot.writeFieldBegin('exc', TType.STRUCT, 1)
      self.exc.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.exc)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class generate_report_args:
  """
  Attributes:
   - report_folder_path
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'report_folder_path', None, None, ), # 1
  )

  def __init__(self, report_folder_path=None,):
    self.report_folder_path = report_folder_path

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.report_folder_path = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('generate_report_args')
    if self.report_folder_path is not None:
      oprot.writeFieldBegin('report_folder_path', TType.STRING, 1)
      oprot.writeString(self.report_folder_path)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.report_folder_path)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class generate_report_result:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('generate_report_result')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class active_drivers_args:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('active_drivers_args')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class active_drivers_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('active_drivers_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class shut_service_args:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('shut_service_args')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class shut_service_result:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('shut_service_result')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)