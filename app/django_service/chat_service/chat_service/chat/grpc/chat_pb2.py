# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chat_service/chat/grpc/chat.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'chat_service/chat/grpc/chat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!chat_service/chat/grpc/chat.proto\x12\x11\x63hat_service.chat\x1a\x1bgoogle/protobuf/empty.proto\"$\n\x16\x43hatRoomDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x15\n\x13\x43hatRoomListRequest\"L\n\x14\x43hatRoomListResponse\x12\x34\n\x07results\x18\x01 \x03(\x0b\x32#.chat_service.chat.ChatRoomResponse\"+\n\x1d\x43hatRoomMessageDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1c\n\x1a\x43hatRoomMessageListRequest\"Z\n\x1b\x43hatRoomMessageListResponse\x12;\n\x07results\x18\x01 \x03(\x0b\x32*.chat_service.chat.ChatRoomMessageResponse\"\xba\x01\n#ChatRoomMessagePartialUpdateRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1e\n\x16_partial_update_fields\x18\x02 \x03(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x11\n\tsender_id\x18\x04 \x01(\x05\x12\x16\n\ttimestamp\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x11\n\tchat_room\x18\x06 \x01(\x05\x42\x05\n\x03_idB\x0c\n\n_timestamp\"\x8d\x01\n\x16\x43hatRoomMessageRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x11\n\tsender_id\x18\x03 \x01(\x05\x12\x16\n\ttimestamp\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x11\n\tchat_room\x18\x05 \x01(\x05\x42\x05\n\x03_idB\x0c\n\n_timestamp\"\x8e\x01\n\x17\x43hatRoomMessageResponse\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x11\n\tsender_id\x18\x03 \x01(\x05\x12\x16\n\ttimestamp\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x11\n\tchat_room\x18\x05 \x01(\x05\x42\x05\n\x03_idB\x0c\n\n_timestamp\",\n\x1e\x43hatRoomMessageRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"G\n/ChatRoomMessageSubscribeChatRoomMessagesRequest\x12\x14\n\x0c\x63hat_room_id\x18\x01 \x01(\x05\"\xae\x01\n\x1c\x43hatRoomPartialUpdateRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1e\n\x16_partial_update_fields\x18\x02 \x03(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x17\n\ncreated_at\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07game_id\x18\x05 \x01(\x05H\x02\x88\x01\x01\x42\x05\n\x03_idB\r\n\x0b_created_atB\n\n\x08_game_id\"\x81\x01\n\x0f\x43hatRoomRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\ncreated_at\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07game_id\x18\x04 \x01(\x05H\x02\x88\x01\x01\x42\x05\n\x03_idB\r\n\x0b_created_atB\n\n\x08_game_id\"\x82\x01\n\x10\x43hatRoomResponse\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\ncreated_at\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07game_id\x18\x04 \x01(\x05H\x02\x88\x01\x01\x42\x05\n\x03_idB\r\n\x0b_created_atB\n\n\x08_game_id\"%\n\x17\x43hatRoomRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"(\n\x1a\x43hatRoomUserDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"9\n&ChatRoomUserGetChatRoomByUserIdRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\x19\n\x17\x43hatRoomUserListRequest\"T\n\x18\x43hatRoomUserListResponse\x12\x38\n\x07results\x18\x01 \x03(\x0b\x32\'.chat_service.chat.ChatRoomUserResponse\"\xa4\x01\n ChatRoomUserPartialUpdateRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1e\n\x16_partial_update_fields\x18\x02 \x03(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x12\x16\n\tjoined_at\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x11\n\tchat_room\x18\x05 \x01(\x05\x42\x05\n\x03_idB\x0c\n\n_joined_at\"w\n\x13\x43hatRoomUserRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x16\n\tjoined_at\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x11\n\tchat_room\x18\x04 \x01(\x05\x42\x05\n\x03_idB\x0c\n\n_joined_at\"x\n\x14\x43hatRoomUserResponse\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x16\n\tjoined_at\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x11\n\tchat_room\x18\x04 \x01(\x05\x42\x05\n\x03_idB\x0c\n\n_joined_at\")\n\x1b\x43hatRoomUserRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\x81\x05\n\x12\x43hatRoomController\x12S\n\x06\x43reate\x12\".chat_service.chat.ChatRoomRequest\x1a#.chat_service.chat.ChatRoomResponse\"\x00\x12N\n\x07\x44\x65stroy\x12).chat_service.chat.ChatRoomDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Y\n\x04List\x12&.chat_service.chat.ChatRoomListRequest\x1a\'.chat_service.chat.ChatRoomListResponse\"\x00\x12N\n\rListChatRooms\x12\x16.google.protobuf.Empty\x1a#.chat_service.chat.ChatRoomResponse\"\x00\x12g\n\rPartialUpdate\x12/.chat_service.chat.ChatRoomPartialUpdateRequest\x1a#.chat_service.chat.ChatRoomResponse\"\x00\x12]\n\x08Retrieve\x12*.chat_service.chat.ChatRoomRetrieveRequest\x1a#.chat_service.chat.ChatRoomResponse\"\x00\x12S\n\x06Update\x12\".chat_service.chat.ChatRoomRequest\x1a#.chat_service.chat.ChatRoomResponse\"\x00\x32\x97\x06\n\x19\x43hatRoomMessageController\x12\x61\n\x06\x43reate\x12).chat_service.chat.ChatRoomMessageRequest\x1a*.chat_service.chat.ChatRoomMessageResponse\"\x00\x12U\n\x07\x44\x65stroy\x12\x30.chat_service.chat.ChatRoomMessageDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12g\n\x04List\x12-.chat_service.chat.ChatRoomMessageListRequest\x1a..chat_service.chat.ChatRoomMessageListResponse\"\x00\x12u\n\rPartialUpdate\x12\x36.chat_service.chat.ChatRoomMessagePartialUpdateRequest\x1a*.chat_service.chat.ChatRoomMessageResponse\"\x00\x12k\n\x08Retrieve\x12\x31.chat_service.chat.ChatRoomMessageRetrieveRequest\x1a*.chat_service.chat.ChatRoomMessageResponse\"\x00\x12\x8f\x01\n\x19SubscribeChatRoomMessages\x12\x42.chat_service.chat.ChatRoomMessageSubscribeChatRoomMessagesRequest\x1a*.chat_service.chat.ChatRoomMessageResponse\"\x00\x30\x01\x12\x61\n\x06Update\x12).chat_service.chat.ChatRoomMessageRequest\x1a*.chat_service.chat.ChatRoomMessageResponse\"\x00\x32\xdc\x05\n\x16\x43hatRoomUserController\x12[\n\x06\x43reate\x12&.chat_service.chat.ChatRoomUserRequest\x1a\'.chat_service.chat.ChatRoomUserResponse\"\x00\x12R\n\x07\x44\x65stroy\x12-.chat_service.chat.ChatRoomUserDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12y\n\x13GetChatRoomByUserId\x12\x39.chat_service.chat.ChatRoomUserGetChatRoomByUserIdRequest\x1a#.chat_service.chat.ChatRoomResponse\"\x00\x30\x01\x12\x61\n\x04List\x12*.chat_service.chat.ChatRoomUserListRequest\x1a+.chat_service.chat.ChatRoomUserListResponse\"\x00\x12o\n\rPartialUpdate\x12\x33.chat_service.chat.ChatRoomUserPartialUpdateRequest\x1a\'.chat_service.chat.ChatRoomUserResponse\"\x00\x12\x65\n\x08Retrieve\x12..chat_service.chat.ChatRoomUserRetrieveRequest\x1a\'.chat_service.chat.ChatRoomUserResponse\"\x00\x12[\n\x06Update\x12&.chat_service.chat.ChatRoomUserRequest\x1a\'.chat_service.chat.ChatRoomUserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_service.chat.grpc.chat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHATROOMDESTROYREQUEST']._serialized_start=85
  _globals['_CHATROOMDESTROYREQUEST']._serialized_end=121
  _globals['_CHATROOMLISTREQUEST']._serialized_start=123
  _globals['_CHATROOMLISTREQUEST']._serialized_end=144
  _globals['_CHATROOMLISTRESPONSE']._serialized_start=146
  _globals['_CHATROOMLISTRESPONSE']._serialized_end=222
  _globals['_CHATROOMMESSAGEDESTROYREQUEST']._serialized_start=224
  _globals['_CHATROOMMESSAGEDESTROYREQUEST']._serialized_end=267
  _globals['_CHATROOMMESSAGELISTREQUEST']._serialized_start=269
  _globals['_CHATROOMMESSAGELISTREQUEST']._serialized_end=297
  _globals['_CHATROOMMESSAGELISTRESPONSE']._serialized_start=299
  _globals['_CHATROOMMESSAGELISTRESPONSE']._serialized_end=389
  _globals['_CHATROOMMESSAGEPARTIALUPDATEREQUEST']._serialized_start=392
  _globals['_CHATROOMMESSAGEPARTIALUPDATEREQUEST']._serialized_end=578
  _globals['_CHATROOMMESSAGEREQUEST']._serialized_start=581
  _globals['_CHATROOMMESSAGEREQUEST']._serialized_end=722
  _globals['_CHATROOMMESSAGERESPONSE']._serialized_start=725
  _globals['_CHATROOMMESSAGERESPONSE']._serialized_end=867
  _globals['_CHATROOMMESSAGERETRIEVEREQUEST']._serialized_start=869
  _globals['_CHATROOMMESSAGERETRIEVEREQUEST']._serialized_end=913
  _globals['_CHATROOMMESSAGESUBSCRIBECHATROOMMESSAGESREQUEST']._serialized_start=915
  _globals['_CHATROOMMESSAGESUBSCRIBECHATROOMMESSAGESREQUEST']._serialized_end=986
  _globals['_CHATROOMPARTIALUPDATEREQUEST']._serialized_start=989
  _globals['_CHATROOMPARTIALUPDATEREQUEST']._serialized_end=1163
  _globals['_CHATROOMREQUEST']._serialized_start=1166
  _globals['_CHATROOMREQUEST']._serialized_end=1295
  _globals['_CHATROOMRESPONSE']._serialized_start=1298
  _globals['_CHATROOMRESPONSE']._serialized_end=1428
  _globals['_CHATROOMRETRIEVEREQUEST']._serialized_start=1430
  _globals['_CHATROOMRETRIEVEREQUEST']._serialized_end=1467
  _globals['_CHATROOMUSERDESTROYREQUEST']._serialized_start=1469
  _globals['_CHATROOMUSERDESTROYREQUEST']._serialized_end=1509
  _globals['_CHATROOMUSERGETCHATROOMBYUSERIDREQUEST']._serialized_start=1511
  _globals['_CHATROOMUSERGETCHATROOMBYUSERIDREQUEST']._serialized_end=1568
  _globals['_CHATROOMUSERLISTREQUEST']._serialized_start=1570
  _globals['_CHATROOMUSERLISTREQUEST']._serialized_end=1595
  _globals['_CHATROOMUSERLISTRESPONSE']._serialized_start=1597
  _globals['_CHATROOMUSERLISTRESPONSE']._serialized_end=1681
  _globals['_CHATROOMUSERPARTIALUPDATEREQUEST']._serialized_start=1684
  _globals['_CHATROOMUSERPARTIALUPDATEREQUEST']._serialized_end=1848
  _globals['_CHATROOMUSERREQUEST']._serialized_start=1850
  _globals['_CHATROOMUSERREQUEST']._serialized_end=1969
  _globals['_CHATROOMUSERRESPONSE']._serialized_start=1971
  _globals['_CHATROOMUSERRESPONSE']._serialized_end=2091
  _globals['_CHATROOMUSERRETRIEVEREQUEST']._serialized_start=2093
  _globals['_CHATROOMUSERRETRIEVEREQUEST']._serialized_end=2134
  _globals['_CHATROOMCONTROLLER']._serialized_start=2137
  _globals['_CHATROOMCONTROLLER']._serialized_end=2778
  _globals['_CHATROOMMESSAGECONTROLLER']._serialized_start=2781
  _globals['_CHATROOMMESSAGECONTROLLER']._serialized_end=3572
  _globals['_CHATROOMUSERCONTROLLER']._serialized_start=3575
  _globals['_CHATROOMUSERCONTROLLER']._serialized_end=4307
# @@protoc_insertion_point(module_scope)
