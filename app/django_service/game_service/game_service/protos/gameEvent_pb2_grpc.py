# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gameEvent_pb2 as gameEvent__pb2


class GameEventServiceStub(object):
    """Service definition for GameEvents
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGameEvent = channel.unary_unary(
                '/transcendence.GameEventService/GetGameEvent',
                request_serializer=gameEvent__pb2.GetGameEventRequest.SerializeToString,
                response_deserializer=gameEvent__pb2.GameEvent.FromString,
                )
        self.CreateGameEvent = channel.unary_unary(
                '/transcendence.GameEventService/CreateGameEvent',
                request_serializer=gameEvent__pb2.CreateGameEventRequest.SerializeToString,
                response_deserializer=gameEvent__pb2.GameEvent.FromString,
                )


class GameEventServiceServicer(object):
    """Service definition for GameEvents
    """

    def GetGameEvent(self, request, context):
        """Get a specific game event by its ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateGameEvent(self, request, context):
        """Create a new game event
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameEventServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGameEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGameEvent,
                    request_deserializer=gameEvent__pb2.GetGameEventRequest.FromString,
                    response_serializer=gameEvent__pb2.GameEvent.SerializeToString,
            ),
            'CreateGameEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGameEvent,
                    request_deserializer=gameEvent__pb2.CreateGameEventRequest.FromString,
                    response_serializer=gameEvent__pb2.GameEvent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'transcendence.GameEventService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GameEventService(object):
    """Service definition for GameEvents
    """

    @staticmethod
    def GetGameEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transcendence.GameEventService/GetGameEvent',
            gameEvent__pb2.GetGameEventRequest.SerializeToString,
            gameEvent__pb2.GameEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateGameEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transcendence.GameEventService/CreateGameEvent',
            gameEvent__pb2.CreateGameEventRequest.SerializeToString,
            gameEvent__pb2.GameEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
