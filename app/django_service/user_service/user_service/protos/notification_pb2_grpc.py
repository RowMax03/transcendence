# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import notification_pb2 as notification__pb2


class NotificationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateNotification = channel.unary_unary(
                '/models.NotificationService/CreateNotification',
                request_serializer=notification__pb2.CreateNotificationRequest.SerializeToString,
                response_deserializer=notification__pb2.Notification.FromString,
                )
        self.GetNotificationById = channel.unary_unary(
                '/models.NotificationService/GetNotificationById',
                request_serializer=notification__pb2.GetNotificationByIdRequest.SerializeToString,
                response_deserializer=notification__pb2.Notification.FromString,
                )
        self.GetNotificationsByUserId = channel.unary_unary(
                '/models.NotificationService/GetNotificationsByUserId',
                request_serializer=notification__pb2.GetNotificationsByUserIdRequest.SerializeToString,
                response_deserializer=notification__pb2.NotificationsResponse.FromString,
                )


class NotificationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNotificationById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNotificationsByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotificationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNotification,
                    request_deserializer=notification__pb2.CreateNotificationRequest.FromString,
                    response_serializer=notification__pb2.Notification.SerializeToString,
            ),
            'GetNotificationById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNotificationById,
                    request_deserializer=notification__pb2.GetNotificationByIdRequest.FromString,
                    response_serializer=notification__pb2.Notification.SerializeToString,
            ),
            'GetNotificationsByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNotificationsByUserId,
                    request_deserializer=notification__pb2.GetNotificationsByUserIdRequest.FromString,
                    response_serializer=notification__pb2.NotificationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'models.NotificationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NotificationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/models.NotificationService/CreateNotification',
            notification__pb2.CreateNotificationRequest.SerializeToString,
            notification__pb2.Notification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNotificationById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/models.NotificationService/GetNotificationById',
            notification__pb2.GetNotificationByIdRequest.SerializeToString,
            notification__pb2.Notification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNotificationsByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/models.NotificationService/GetNotificationsByUserId',
            notification__pb2.GetNotificationsByUserIdRequest.SerializeToString,
            notification__pb2.NotificationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
