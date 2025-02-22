# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dsbd.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'dsbd.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndsbd.proto\"!\n\x10LoginUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"H\n\x13RegisterUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12\x12\n\nmessage_id\x18\x03 \x01(\t\"F\n\x11UpdateUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12\x12\n\nmessage_id\x18\x03 \x01(\t\"S\n\x1bUpdateUserThresholdsRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x12\n\nhigh_value\x18\x02 \x01(\x02\x12\x11\n\tlow_value\x18\x03 \x01(\x02\"R\n\x1aResetUserThresholdsRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x12\n\nhigh_value\x18\x02 \x01(\x05\x12\x11\n\tlow_value\x18\x03 \x01(\x05\"\"\n\x11\x44\x65leteUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"!\n\x10GetTickerRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"=\n\x17GetTickerAverageRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x13\n\x0blastXValues\x18\x02 \x01(\x05\"0\n\x0cUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"A\n\x0eTickerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x02\x32\xd0\x03\n\x0b\x44SBDService\x12-\n\tLoginUser\x12\x11.LoginUserRequest\x1a\r.UserResponse\x12\x33\n\x0cRegisterUser\x12\x14.RegisterUserRequest\x1a\r.UserResponse\x12/\n\nUpdateUser\x12\x12.UpdateUserRequest\x1a\r.UserResponse\x12/\n\nDeleteUser\x12\x12.DeleteUserRequest\x1a\r.UserResponse\x12\x34\n\x0eGetTickerValue\x12\x11.GetTickerRequest\x1a\x0f.TickerResponse\x12=\n\x10GetTickerAverage\x12\x18.GetTickerAverageRequest\x1a\x0f.TickerResponse\x12\x43\n\x14UpdateUserThresholds\x12\x1c.UpdateUserThresholdsRequest\x1a\r.UserResponse\x12\x41\n\x13ResetUserThresholds\x12\x1b.ResetUserThresholdsRequest\x1a\r.UserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dsbd_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOGINUSERREQUEST']._serialized_start=14
  _globals['_LOGINUSERREQUEST']._serialized_end=47
  _globals['_REGISTERUSERREQUEST']._serialized_start=49
  _globals['_REGISTERUSERREQUEST']._serialized_end=121
  _globals['_UPDATEUSERREQUEST']._serialized_start=123
  _globals['_UPDATEUSERREQUEST']._serialized_end=193
  _globals['_UPDATEUSERTHRESHOLDSREQUEST']._serialized_start=195
  _globals['_UPDATEUSERTHRESHOLDSREQUEST']._serialized_end=278
  _globals['_RESETUSERTHRESHOLDSREQUEST']._serialized_start=280
  _globals['_RESETUSERTHRESHOLDSREQUEST']._serialized_end=362
  _globals['_DELETEUSERREQUEST']._serialized_start=364
  _globals['_DELETEUSERREQUEST']._serialized_end=398
  _globals['_GETTICKERREQUEST']._serialized_start=400
  _globals['_GETTICKERREQUEST']._serialized_end=433
  _globals['_GETTICKERAVERAGEREQUEST']._serialized_start=435
  _globals['_GETTICKERAVERAGEREQUEST']._serialized_end=496
  _globals['_USERRESPONSE']._serialized_start=498
  _globals['_USERRESPONSE']._serialized_end=546
  _globals['_TICKERRESPONSE']._serialized_start=548
  _globals['_TICKERRESPONSE']._serialized_end=613
  _globals['_DSBDSERVICE']._serialized_start=616
  _globals['_DSBDSERVICE']._serialized_end=1080
# @@protoc_insertion_point(module_scope)
