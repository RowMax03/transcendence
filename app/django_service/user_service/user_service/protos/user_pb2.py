# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x06models\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf7\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04mail\x18\x03 \x01(\t\x12\x0f\n\x07\x62locked\x18\x05 \x01(\x08\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07role_id\x18\x08 \x01(\x05\x12.\n\nlast_login\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rlast_login_ip\x18\n \x01(\t\"t\n\x11\x43reateUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04mail\x18\x03 \x01(\t\x12\x0f\n\x07\x62locked\x18\x05 \x01(\x08\x12\x0f\n\x07role_id\x18\x06 \x01(\x05\x12\x15\n\rlast_login_ip\x18\x07 \x01(\t\"\x1c\n\x0eGetUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"*\n\x17GetUsersByRoleIdRequest\x12\x0f\n\x07role_id\x18\x01 \x01(\x05\",\n\rUsersResponse\x12\x1b\n\x05users\x18\x01 \x03(\x0b\x32\x0c.models.User2\xc1\x01\n\x0bUserService\x12\x35\n\nCreateUser\x12\x19.models.CreateUserRequest\x1a\x0c.models.User\x12/\n\x07GetUser\x12\x16.models.GetUserRequest\x1a\x0c.models.User\x12J\n\x10GetUsersByRoleId\x12\x1f.models.GetUsersByRoleIdRequest\x1a\x15.models.UsersResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=56
  _USER._serialized_end=303
  _CREATEUSERREQUEST._serialized_start=305
  _CREATEUSERREQUEST._serialized_end=421
  _GETUSERREQUEST._serialized_start=423
  _GETUSERREQUEST._serialized_end=451
  _GETUSERSBYROLEIDREQUEST._serialized_start=453
  _GETUSERSBYROLEIDREQUEST._serialized_end=495
  _USERSRESPONSE._serialized_start=497
  _USERSRESPONSE._serialized_end=541
  _USERSERVICE._serialized_start=544
  _USERSERVICE._serialized_end=737
# @@protoc_insertion_point(module_scope)
