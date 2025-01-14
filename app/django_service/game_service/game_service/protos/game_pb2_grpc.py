# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import game_pb2 as game__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class GameServiceStub(object):
    """Service definition for Games
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGame = channel.unary_unary(
                '/transcendence.GameService/GetGame',
                request_serializer=game__pb2.GetGameRequest.SerializeToString,
                response_deserializer=game__pb2.Game.FromString,
                )
        self.GetOnGoingGameByUser = channel.unary_unary(
                '/transcendence.GameService/GetOnGoingGameByUser',
                request_serializer=game__pb2.GetOnGoingGameByUserRequest.SerializeToString,
                response_deserializer=game__pb2.Game.FromString,
                )
        self.GetOngoingGames = channel.unary_unary(
                '/transcendence.GameService/GetOngoingGames',
                request_serializer=game__pb2.GetOngoingGamesRequest.SerializeToString,
                response_deserializer=game__pb2.GetOngoingGamesResponse.FromString,
                )
        self.CreateGame = channel.unary_unary(
                '/transcendence.GameService/CreateGame',
                request_serializer=game__pb2.CreateGameRequest.SerializeToString,
                response_deserializer=game__pb2.Game.FromString,
                )
        self.StartGame = channel.unary_unary(
                '/transcendence.GameService/StartGame',
                request_serializer=game__pb2.StartGameRequest.SerializeToString,
                response_deserializer=game__pb2.StartGameResponse.FromString,
                )
        self.HandleGameFinished = channel.unary_unary(
                '/transcendence.GameService/HandleGameFinished',
                request_serializer=game__pb2.GameFinishedRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GameReady = channel.unary_stream(
                '/transcendence.GameService/GameReady',
                request_serializer=game__pb2.GameReadyRequest.SerializeToString,
                response_deserializer=game__pb2.Game.FromString,
                )


class GameServiceServicer(object):
    """Service definition for Games
    """

    def GetGame(self, request, context):
        """Get a specific game by its ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOnGoingGameByUser(self, request, context):
        """Get an on going game by user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOngoingGames(self, request, context):
        """Get a list of ongoing games (not finished)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateGame(self, request, context):
        """Create a new game
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartGame(self, request, context):
        """Start a game and provide WebSocket updates URL
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleGameFinished(self, request, context):
        """Receive update if the game is finished
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GameReady(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGame': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGame,
                    request_deserializer=game__pb2.GetGameRequest.FromString,
                    response_serializer=game__pb2.Game.SerializeToString,
            ),
            'GetOnGoingGameByUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOnGoingGameByUser,
                    request_deserializer=game__pb2.GetOnGoingGameByUserRequest.FromString,
                    response_serializer=game__pb2.Game.SerializeToString,
            ),
            'GetOngoingGames': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOngoingGames,
                    request_deserializer=game__pb2.GetOngoingGamesRequest.FromString,
                    response_serializer=game__pb2.GetOngoingGamesResponse.SerializeToString,
            ),
            'CreateGame': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGame,
                    request_deserializer=game__pb2.CreateGameRequest.FromString,
                    response_serializer=game__pb2.Game.SerializeToString,
            ),
            'StartGame': grpc.unary_unary_rpc_method_handler(
                    servicer.StartGame,
                    request_deserializer=game__pb2.StartGameRequest.FromString,
                    response_serializer=game__pb2.StartGameResponse.SerializeToString,
            ),
            'HandleGameFinished': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleGameFinished,
                    request_deserializer=game__pb2.GameFinishedRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GameReady': grpc.unary_stream_rpc_method_handler(
                    servicer.GameReady,
                    request_deserializer=game__pb2.GameReadyRequest.FromString,
                    response_serializer=game__pb2.Game.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'transcendence.GameService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GameService(object):
    """Service definition for Games
    """

    @staticmethod
    def GetGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transcendence.GameService/GetGame',
            game__pb2.GetGameRequest.SerializeToString,
            game__pb2.Game.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOnGoingGameByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transcendence.GameService/GetOnGoingGameByUser',
            game__pb2.GetOnGoingGameByUserRequest.SerializeToString,
            game__pb2.Game.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOngoingGames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transcendence.GameService/GetOngoingGames',
            game__pb2.GetOngoingGamesRequest.SerializeToString,
            game__pb2.GetOngoingGamesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transcendence.GameService/CreateGame',
            game__pb2.CreateGameRequest.SerializeToString,
            game__pb2.Game.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transcendence.GameService/StartGame',
            game__pb2.StartGameRequest.SerializeToString,
            game__pb2.StartGameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleGameFinished(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transcendence.GameService/HandleGameFinished',
            game__pb2.GameFinishedRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GameReady(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/transcendence.GameService/GameReady',
            game__pb2.GameReadyRequest.SerializeToString,
            game__pb2.Game.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
