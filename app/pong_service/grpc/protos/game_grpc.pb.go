// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v3.21.12
// source: grpc/protos/game.proto

package protos

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	GameService_GetGame_FullMethodName              = "/transcendence.GameService/GetGame"
	GameService_GetOnGoingGameByUser_FullMethodName = "/transcendence.GameService/GetOnGoingGameByUser"
	GameService_GetOngoingGames_FullMethodName      = "/transcendence.GameService/GetOngoingGames"
	GameService_CreateGame_FullMethodName           = "/transcendence.GameService/CreateGame"
	GameService_CreateFriendGame_FullMethodName     = "/transcendence.GameService/CreateFriendGame"
	GameService_StartGame_FullMethodName            = "/transcendence.GameService/StartGame"
	GameService_HandleGameFinished_FullMethodName   = "/transcendence.GameService/HandleGameFinished"
	GameService_GameReady_FullMethodName            = "/transcendence.GameService/GameReady"
	GameService_UpdateGameState_FullMethodName      = "/transcendence.GameService/UpdateGameState"
)

// GameServiceClient is the client API for GameService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
//
// Service definition for Games
type GameServiceClient interface {
	// Get a specific game by its ID
	GetGame(ctx context.Context, in *GetGameRequest, opts ...grpc.CallOption) (*Game, error)
	// Get an on going game by user
	GetOnGoingGameByUser(ctx context.Context, in *GetOnGoingGameByUserRequest, opts ...grpc.CallOption) (*Game, error)
	// Get a list of ongoing games (not finished)
	GetOngoingGames(ctx context.Context, in *GetOngoingGamesRequest, opts ...grpc.CallOption) (*GetOngoingGamesResponse, error)
	// Create a new game
	CreateGame(ctx context.Context, in *CreateGameRequest, opts ...grpc.CallOption) (*Game, error)
	CreateFriendGame(ctx context.Context, in *CreateFriendGameRequest, opts ...grpc.CallOption) (*Game, error)
	StartGame(ctx context.Context, in *StartGameRequest, opts ...grpc.CallOption) (*StartGameResponse, error)
	HandleGameFinished(ctx context.Context, in *GameFinishedRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	GameReady(ctx context.Context, in *GameReadyRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[Game], error)
	UpdateGameState(ctx context.Context, in *UpdateGameStateRequest, opts ...grpc.CallOption) (*Game, error)
}

type gameServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewGameServiceClient(cc grpc.ClientConnInterface) GameServiceClient {
	return &gameServiceClient{cc}
}

func (c *gameServiceClient) GetGame(ctx context.Context, in *GetGameRequest, opts ...grpc.CallOption) (*Game, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Game)
	err := c.cc.Invoke(ctx, GameService_GetGame_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gameServiceClient) GetOnGoingGameByUser(ctx context.Context, in *GetOnGoingGameByUserRequest, opts ...grpc.CallOption) (*Game, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Game)
	err := c.cc.Invoke(ctx, GameService_GetOnGoingGameByUser_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gameServiceClient) GetOngoingGames(ctx context.Context, in *GetOngoingGamesRequest, opts ...grpc.CallOption) (*GetOngoingGamesResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetOngoingGamesResponse)
	err := c.cc.Invoke(ctx, GameService_GetOngoingGames_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gameServiceClient) CreateGame(ctx context.Context, in *CreateGameRequest, opts ...grpc.CallOption) (*Game, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Game)
	err := c.cc.Invoke(ctx, GameService_CreateGame_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gameServiceClient) CreateFriendGame(ctx context.Context, in *CreateFriendGameRequest, opts ...grpc.CallOption) (*Game, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Game)
	err := c.cc.Invoke(ctx, GameService_CreateFriendGame_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gameServiceClient) StartGame(ctx context.Context, in *StartGameRequest, opts ...grpc.CallOption) (*StartGameResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(StartGameResponse)
	err := c.cc.Invoke(ctx, GameService_StartGame_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gameServiceClient) HandleGameFinished(ctx context.Context, in *GameFinishedRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, GameService_HandleGameFinished_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gameServiceClient) GameReady(ctx context.Context, in *GameReadyRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[Game], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &GameService_ServiceDesc.Streams[0], GameService_GameReady_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[GameReadyRequest, Game]{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type GameService_GameReadyClient = grpc.ServerStreamingClient[Game]

func (c *gameServiceClient) UpdateGameState(ctx context.Context, in *UpdateGameStateRequest, opts ...grpc.CallOption) (*Game, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Game)
	err := c.cc.Invoke(ctx, GameService_UpdateGameState_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// GameServiceServer is the server API for GameService service.
// All implementations must embed UnimplementedGameServiceServer
// for forward compatibility.
//
// Service definition for Games
type GameServiceServer interface {
	// Get a specific game by its ID
	GetGame(context.Context, *GetGameRequest) (*Game, error)
	// Get an on going game by user
	GetOnGoingGameByUser(context.Context, *GetOnGoingGameByUserRequest) (*Game, error)
	// Get a list of ongoing games (not finished)
	GetOngoingGames(context.Context, *GetOngoingGamesRequest) (*GetOngoingGamesResponse, error)
	// Create a new game
	CreateGame(context.Context, *CreateGameRequest) (*Game, error)
	CreateFriendGame(context.Context, *CreateFriendGameRequest) (*Game, error)
	StartGame(context.Context, *StartGameRequest) (*StartGameResponse, error)
	HandleGameFinished(context.Context, *GameFinishedRequest) (*emptypb.Empty, error)
	GameReady(*GameReadyRequest, grpc.ServerStreamingServer[Game]) error
	UpdateGameState(context.Context, *UpdateGameStateRequest) (*Game, error)
	mustEmbedUnimplementedGameServiceServer()
}

// UnimplementedGameServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedGameServiceServer struct{}

func (UnimplementedGameServiceServer) GetGame(context.Context, *GetGameRequest) (*Game, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetGame not implemented")
}
func (UnimplementedGameServiceServer) GetOnGoingGameByUser(context.Context, *GetOnGoingGameByUserRequest) (*Game, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetOnGoingGameByUser not implemented")
}
func (UnimplementedGameServiceServer) GetOngoingGames(context.Context, *GetOngoingGamesRequest) (*GetOngoingGamesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetOngoingGames not implemented")
}
func (UnimplementedGameServiceServer) CreateGame(context.Context, *CreateGameRequest) (*Game, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateGame not implemented")
}
func (UnimplementedGameServiceServer) CreateFriendGame(context.Context, *CreateFriendGameRequest) (*Game, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateFriendGame not implemented")
}
func (UnimplementedGameServiceServer) StartGame(context.Context, *StartGameRequest) (*StartGameResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method StartGame not implemented")
}
func (UnimplementedGameServiceServer) HandleGameFinished(context.Context, *GameFinishedRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method HandleGameFinished not implemented")
}
func (UnimplementedGameServiceServer) GameReady(*GameReadyRequest, grpc.ServerStreamingServer[Game]) error {
	return status.Errorf(codes.Unimplemented, "method GameReady not implemented")
}
func (UnimplementedGameServiceServer) UpdateGameState(context.Context, *UpdateGameStateRequest) (*Game, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateGameState not implemented")
}
func (UnimplementedGameServiceServer) mustEmbedUnimplementedGameServiceServer() {}
func (UnimplementedGameServiceServer) testEmbeddedByValue()                     {}

// UnsafeGameServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to GameServiceServer will
// result in compilation errors.
type UnsafeGameServiceServer interface {
	mustEmbedUnimplementedGameServiceServer()
}

func RegisterGameServiceServer(s grpc.ServiceRegistrar, srv GameServiceServer) {
	// If the following call pancis, it indicates UnimplementedGameServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&GameService_ServiceDesc, srv)
}

func _GameService_GetGame_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetGameRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServiceServer).GetGame(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GameService_GetGame_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServiceServer).GetGame(ctx, req.(*GetGameRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GameService_GetOnGoingGameByUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetOnGoingGameByUserRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServiceServer).GetOnGoingGameByUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GameService_GetOnGoingGameByUser_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServiceServer).GetOnGoingGameByUser(ctx, req.(*GetOnGoingGameByUserRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GameService_GetOngoingGames_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetOngoingGamesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServiceServer).GetOngoingGames(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GameService_GetOngoingGames_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServiceServer).GetOngoingGames(ctx, req.(*GetOngoingGamesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GameService_CreateGame_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateGameRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServiceServer).CreateGame(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GameService_CreateGame_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServiceServer).CreateGame(ctx, req.(*CreateGameRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GameService_CreateFriendGame_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateFriendGameRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServiceServer).CreateFriendGame(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GameService_CreateFriendGame_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServiceServer).CreateFriendGame(ctx, req.(*CreateFriendGameRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GameService_StartGame_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(StartGameRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServiceServer).StartGame(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GameService_StartGame_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServiceServer).StartGame(ctx, req.(*StartGameRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GameService_HandleGameFinished_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GameFinishedRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServiceServer).HandleGameFinished(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GameService_HandleGameFinished_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServiceServer).HandleGameFinished(ctx, req.(*GameFinishedRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GameService_GameReady_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(GameReadyRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(GameServiceServer).GameReady(m, &grpc.GenericServerStream[GameReadyRequest, Game]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type GameService_GameReadyServer = grpc.ServerStreamingServer[Game]

func _GameService_UpdateGameState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateGameStateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServiceServer).UpdateGameState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GameService_UpdateGameState_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServiceServer).UpdateGameState(ctx, req.(*UpdateGameStateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// GameService_ServiceDesc is the grpc.ServiceDesc for GameService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var GameService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "transcendence.GameService",
	HandlerType: (*GameServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetGame",
			Handler:    _GameService_GetGame_Handler,
		},
		{
			MethodName: "GetOnGoingGameByUser",
			Handler:    _GameService_GetOnGoingGameByUser_Handler,
		},
		{
			MethodName: "GetOngoingGames",
			Handler:    _GameService_GetOngoingGames_Handler,
		},
		{
			MethodName: "CreateGame",
			Handler:    _GameService_CreateGame_Handler,
		},
		{
			MethodName: "CreateFriendGame",
			Handler:    _GameService_CreateFriendGame_Handler,
		},
		{
			MethodName: "StartGame",
			Handler:    _GameService_StartGame_Handler,
		},
		{
			MethodName: "HandleGameFinished",
			Handler:    _GameService_HandleGameFinished_Handler,
		},
		{
			MethodName: "UpdateGameState",
			Handler:    _GameService_UpdateGameState_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "GameReady",
			Handler:       _GameService_GameReady_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "grpc/protos/game.proto",
}
