// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.1
// 	protoc        v3.21.12
// source: grpc/protos/gameEvent.proto

package protos

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// Message to define a GameEvent
type GameEvent struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Id            int32                  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	GameId        int32                  `protobuf:"varint,2,opt,name=game_id,json=gameId,proto3" json:"game_id,omitempty"`         // FK to Game
	EventType     string                 `protobuf:"bytes,3,opt,name=event_type,json=eventType,proto3" json:"event_type,omitempty"` // Type of the event
	EventData     string                 `protobuf:"bytes,4,opt,name=event_data,json=eventData,proto3" json:"event_data,omitempty"` // Data associated with the event
	Timestamp     *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=timestamp,proto3" json:"timestamp,omitempty"`                  // Time of the event
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GameEvent) Reset() {
	*x = GameEvent{}
	mi := &file_grpc_protos_gameEvent_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GameEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GameEvent) ProtoMessage() {}

func (x *GameEvent) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_protos_gameEvent_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GameEvent.ProtoReflect.Descriptor instead.
func (*GameEvent) Descriptor() ([]byte, []int) {
	return file_grpc_protos_gameEvent_proto_rawDescGZIP(), []int{0}
}

func (x *GameEvent) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *GameEvent) GetGameId() int32 {
	if x != nil {
		return x.GameId
	}
	return 0
}

func (x *GameEvent) GetEventType() string {
	if x != nil {
		return x.EventType
	}
	return ""
}

func (x *GameEvent) GetEventData() string {
	if x != nil {
		return x.EventData
	}
	return ""
}

func (x *GameEvent) GetTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.Timestamp
	}
	return nil
}

// Request to get a specific game event by its ID
type GetGameEventRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	GameEventId   int32                  `protobuf:"varint,1,opt,name=game_event_id,json=gameEventId,proto3" json:"game_event_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetGameEventRequest) Reset() {
	*x = GetGameEventRequest{}
	mi := &file_grpc_protos_gameEvent_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetGameEventRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetGameEventRequest) ProtoMessage() {}

func (x *GetGameEventRequest) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_protos_gameEvent_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetGameEventRequest.ProtoReflect.Descriptor instead.
func (*GetGameEventRequest) Descriptor() ([]byte, []int) {
	return file_grpc_protos_gameEvent_proto_rawDescGZIP(), []int{1}
}

func (x *GetGameEventRequest) GetGameEventId() int32 {
	if x != nil {
		return x.GameEventId
	}
	return 0
}

// Request to create a new game event
type CreateGameEventRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	GameId        int32                  `protobuf:"varint,1,opt,name=game_id,json=gameId,proto3" json:"game_id,omitempty"`         // FK to Game
	EventType     string                 `protobuf:"bytes,2,opt,name=event_type,json=eventType,proto3" json:"event_type,omitempty"` // Type of the event
	EventData     string                 `protobuf:"bytes,3,opt,name=event_data,json=eventData,proto3" json:"event_data,omitempty"` // Data associated with the event
	Timestamp     *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=timestamp,proto3" json:"timestamp,omitempty"`                  // Time of the event
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CreateGameEventRequest) Reset() {
	*x = CreateGameEventRequest{}
	mi := &file_grpc_protos_gameEvent_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreateGameEventRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateGameEventRequest) ProtoMessage() {}

func (x *CreateGameEventRequest) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_protos_gameEvent_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateGameEventRequest.ProtoReflect.Descriptor instead.
func (*CreateGameEventRequest) Descriptor() ([]byte, []int) {
	return file_grpc_protos_gameEvent_proto_rawDescGZIP(), []int{2}
}

func (x *CreateGameEventRequest) GetGameId() int32 {
	if x != nil {
		return x.GameId
	}
	return 0
}

func (x *CreateGameEventRequest) GetEventType() string {
	if x != nil {
		return x.EventType
	}
	return ""
}

func (x *CreateGameEventRequest) GetEventData() string {
	if x != nil {
		return x.EventData
	}
	return ""
}

func (x *CreateGameEventRequest) GetTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.Timestamp
	}
	return nil
}

var File_grpc_protos_gameEvent_proto protoreflect.FileDescriptor

var file_grpc_protos_gameEvent_proto_rawDesc = []byte{
	0x0a, 0x1b, 0x67, 0x72, 0x70, 0x63, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x67, 0x61,
	0x6d, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x0d, 0x74,
	0x72, 0x61, 0x6e, 0x73, 0x63, 0x65, 0x6e, 0x64, 0x65, 0x6e, 0x63, 0x65, 0x1a, 0x1f, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69,
	0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xac, 0x01,
	0x0a, 0x09, 0x47, 0x61, 0x6d, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x17, 0x0a, 0x07, 0x67,
	0x61, 0x6d, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x06, 0x67, 0x61,
	0x6d, 0x65, 0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x74, 0x79,
	0x70, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x54,
	0x79, 0x70, 0x65, 0x12, 0x1d, 0x0a, 0x0a, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x64, 0x61, 0x74,
	0x61, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x44, 0x61,
	0x74, 0x61, 0x12, 0x38, 0x0a, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18,
	0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x52, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x22, 0x39, 0x0a, 0x13,
	0x47, 0x65, 0x74, 0x47, 0x61, 0x6d, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x12, 0x22, 0x0a, 0x0d, 0x67, 0x61, 0x6d, 0x65, 0x5f, 0x65, 0x76, 0x65, 0x6e,
	0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0b, 0x67, 0x61, 0x6d, 0x65,
	0x45, 0x76, 0x65, 0x6e, 0x74, 0x49, 0x64, 0x22, 0xa9, 0x01, 0x0a, 0x16, 0x43, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x47, 0x61, 0x6d, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x12, 0x17, 0x0a, 0x07, 0x67, 0x61, 0x6d, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x05, 0x52, 0x06, 0x67, 0x61, 0x6d, 0x65, 0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x65,
	0x76, 0x65, 0x6e, 0x74, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x09, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x54, 0x79, 0x70, 0x65, 0x12, 0x1d, 0x0a, 0x0a, 0x65, 0x76,
	0x65, 0x6e, 0x74, 0x5f, 0x64, 0x61, 0x74, 0x61, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x44, 0x61, 0x74, 0x61, 0x12, 0x38, 0x0a, 0x09, 0x74, 0x69, 0x6d,
	0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67,
	0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54,
	0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74,
	0x61, 0x6d, 0x70, 0x32, 0xb4, 0x01, 0x0a, 0x10, 0x47, 0x61, 0x6d, 0x65, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x4c, 0x0a, 0x0c, 0x47, 0x65, 0x74, 0x47,
	0x61, 0x6d, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x22, 0x2e, 0x74, 0x72, 0x61, 0x6e, 0x73,
	0x63, 0x65, 0x6e, 0x64, 0x65, 0x6e, 0x63, 0x65, 0x2e, 0x47, 0x65, 0x74, 0x47, 0x61, 0x6d, 0x65,
	0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x18, 0x2e, 0x74,
	0x72, 0x61, 0x6e, 0x73, 0x63, 0x65, 0x6e, 0x64, 0x65, 0x6e, 0x63, 0x65, 0x2e, 0x47, 0x61, 0x6d,
	0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x52, 0x0a, 0x0f, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x47, 0x61, 0x6d, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x25, 0x2e, 0x74, 0x72, 0x61, 0x6e,
	0x73, 0x63, 0x65, 0x6e, 0x64, 0x65, 0x6e, 0x63, 0x65, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x47, 0x61, 0x6d, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x1a, 0x18, 0x2e, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x63, 0x65, 0x6e, 0x64, 0x65, 0x6e, 0x63, 0x65,
	0x2e, 0x47, 0x61, 0x6d, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x42, 0x0a, 0x5a, 0x08, 0x2e, 0x2f,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_grpc_protos_gameEvent_proto_rawDescOnce sync.Once
	file_grpc_protos_gameEvent_proto_rawDescData = file_grpc_protos_gameEvent_proto_rawDesc
)

func file_grpc_protos_gameEvent_proto_rawDescGZIP() []byte {
	file_grpc_protos_gameEvent_proto_rawDescOnce.Do(func() {
		file_grpc_protos_gameEvent_proto_rawDescData = protoimpl.X.CompressGZIP(file_grpc_protos_gameEvent_proto_rawDescData)
	})
	return file_grpc_protos_gameEvent_proto_rawDescData
}

var file_grpc_protos_gameEvent_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_grpc_protos_gameEvent_proto_goTypes = []any{
	(*GameEvent)(nil),              // 0: transcendence.GameEvent
	(*GetGameEventRequest)(nil),    // 1: transcendence.GetGameEventRequest
	(*CreateGameEventRequest)(nil), // 2: transcendence.CreateGameEventRequest
	(*timestamppb.Timestamp)(nil),  // 3: google.protobuf.Timestamp
}
var file_grpc_protos_gameEvent_proto_depIdxs = []int32{
	3, // 0: transcendence.GameEvent.timestamp:type_name -> google.protobuf.Timestamp
	3, // 1: transcendence.CreateGameEventRequest.timestamp:type_name -> google.protobuf.Timestamp
	1, // 2: transcendence.GameEventService.GetGameEvent:input_type -> transcendence.GetGameEventRequest
	2, // 3: transcendence.GameEventService.CreateGameEvent:input_type -> transcendence.CreateGameEventRequest
	0, // 4: transcendence.GameEventService.GetGameEvent:output_type -> transcendence.GameEvent
	0, // 5: transcendence.GameEventService.CreateGameEvent:output_type -> transcendence.GameEvent
	4, // [4:6] is the sub-list for method output_type
	2, // [2:4] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_grpc_protos_gameEvent_proto_init() }
func file_grpc_protos_gameEvent_proto_init() {
	if File_grpc_protos_gameEvent_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_grpc_protos_gameEvent_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_grpc_protos_gameEvent_proto_goTypes,
		DependencyIndexes: file_grpc_protos_gameEvent_proto_depIdxs,
		MessageInfos:      file_grpc_protos_gameEvent_proto_msgTypes,
	}.Build()
	File_grpc_protos_gameEvent_proto = out.File
	file_grpc_protos_gameEvent_proto_rawDesc = nil
	file_grpc_protos_gameEvent_proto_goTypes = nil
	file_grpc_protos_gameEvent_proto_depIdxs = nil
}
