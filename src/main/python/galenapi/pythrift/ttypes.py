#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class SpecNotFoundException(TException):
  """
  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

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
          self.message = iprot.readString();
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
    oprot.writeStructBegin('SpecNotFoundException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RemoteWebDriverException(TException):
  """
  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

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
          self.message = iprot.readString();
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
    oprot.writeStructBegin('RemoteWebDriverException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ResponseValueType:
  """
  Attributes:
   - string_cap
   - bool_cap
   - set_cap
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'string_cap', None, None, ), # 1
    (2, TType.BOOL, 'bool_cap', None, None, ), # 2
    (3, TType.SET, 'set_cap', (TType.STRING,None), None, ), # 3
  )

  def __init__(self, string_cap=None, bool_cap=None, set_cap=None,):
    self.string_cap = string_cap
    self.bool_cap = bool_cap
    self.set_cap = set_cap

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
          self.string_cap = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.bool_cap = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.SET:
          self.set_cap = set()
          (_etype3, _size0) = iprot.readSetBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.set_cap.add(_elem5)
          iprot.readSetEnd()
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
    oprot.writeStructBegin('ResponseValueType')
    if self.string_cap is not None:
      oprot.writeFieldBegin('string_cap', TType.STRING, 1)
      oprot.writeString(self.string_cap)
      oprot.writeFieldEnd()
    if self.bool_cap is not None:
      oprot.writeFieldBegin('bool_cap', TType.BOOL, 2)
      oprot.writeBool(self.bool_cap)
      oprot.writeFieldEnd()
    if self.set_cap is not None:
      oprot.writeFieldBegin('set_cap', TType.SET, 3)
      oprot.writeSetBegin(TType.STRING, len(self.set_cap))
      for iter6 in self.set_cap:
        oprot.writeString(iter6)
      oprot.writeSetEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.string_cap)
    value = (value * 31) ^ hash(self.bool_cap)
    value = (value * 31) ^ hash(self.set_cap)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Response:
  """
  Attributes:
   - value
   - session_id
   - status
   - state
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'value', (ResponseValueType, ResponseValueType.thrift_spec), None, ), # 1
    (2, TType.STRING, 'session_id', None, None, ), # 2
    (3, TType.I32, 'status', None, None, ), # 3
    (4, TType.STRING, 'state', None, None, ), # 4
  )

  def __init__(self, value=None, session_id=None, status=None, state=None,):
    self.value = value
    self.session_id = session_id
    self.status = status
    self.state = state

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
        if ftype == TType.STRUCT:
          self.value = ResponseValueType()
          self.value.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.session_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.status = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.state = iprot.readString();
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
    oprot.writeStructBegin('Response')
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.STRUCT, 1)
      self.value.write(oprot)
      oprot.writeFieldEnd()
    if self.session_id is not None:
      oprot.writeFieldBegin('session_id', TType.STRING, 2)
      oprot.writeString(self.session_id)
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I32, 3)
      oprot.writeI32(self.status)
      oprot.writeFieldEnd()
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.STRING, 4)
      oprot.writeString(self.state)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.value)
    value = (value * 31) ^ hash(self.session_id)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.state)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
