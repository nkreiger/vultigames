# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='game',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\ngame.proto\x12\x04game\"\x1e\n\rStatusRequest\x12\r\n\x05\x63heck\x18\x01 \x01(\t\" \n\x0eStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2=\n\x06Status\x12\x33\n\x04test\x12\x13.game.StatusRequest\x1a\x14.game.StatusResponse\"\x00\x62\x06proto3'
)




_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='game.StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='check', full_name='game.StatusRequest.check', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=50,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='game.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='game.StatusResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:game.StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:game.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)



_STATUS = _descriptor.ServiceDescriptor(
  name='Status',
  full_name='game.Status',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=86,
  serialized_end=147,
  methods=[
  _descriptor.MethodDescriptor(
    name='test',
    full_name='game.Status.test',
    index=0,
    containing_service=None,
    input_type=_STATUSREQUEST,
    output_type=_STATUSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATUS)

DESCRIPTOR.services_by_name['Status'] = _STATUS

# @@protoc_insertion_point(module_scope)
