# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04\x63hat\x1a\x1fgoogle/protobuf/timestamp.proto\"\x82\x01\n\x0b\x43hatMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x11\n\tsender_id\x18\x03 \x01(\x05\x12\x14\n\x0c\x63hat_room_id\x18\x04 \x01(\x05\x12-\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"e\n\x08\x43hatRoom\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07game_id\x18\x04 \x01(\x05\"6\n\x15\x43reateChatRoomRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\x05\" \n\x12GetChatRoomRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty2\xb9\x01\n\x0b\x43hatService\x12=\n\x0e\x43reateChatRoom\x12\x1b.chat.CreateChatRoomRequest\x1a\x0e.chat.ChatRoom\x12;\n\x0fGetChatRoomById\x12\x18.chat.GetChatRoomRequest\x1a\x0e.chat.ChatRoom\x12.\n\rListChatRooms\x12\x0b.chat.Empty\x1a\x0e.chat.ChatRoom0\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHATMESSAGE._serialized_start=54
  _CHATMESSAGE._serialized_end=184
  _CHATROOM._serialized_start=186
  _CHATROOM._serialized_end=287
  _CREATECHATROOMREQUEST._serialized_start=289
  _CREATECHATROOMREQUEST._serialized_end=343
  _GETCHATROOMREQUEST._serialized_start=345
  _GETCHATROOMREQUEST._serialized_end=377
  _EMPTY._serialized_start=379
  _EMPTY._serialized_end=386
  _CHATSERVICE._serialized_start=389
  _CHATSERVICE._serialized_end=574
# @@protoc_insertion_point(module_scope)
