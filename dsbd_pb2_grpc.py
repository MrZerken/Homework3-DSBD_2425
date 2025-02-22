# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import dsbd_pb2 as dsbd__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in dsbd_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DSBDServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoginUser = channel.unary_unary(
                '/DSBDService/LoginUser',
                request_serializer=dsbd__pb2.LoginUserRequest.SerializeToString,
                response_deserializer=dsbd__pb2.UserResponse.FromString,
                _registered_method=True)
        self.RegisterUser = channel.unary_unary(
                '/DSBDService/RegisterUser',
                request_serializer=dsbd__pb2.RegisterUserRequest.SerializeToString,
                response_deserializer=dsbd__pb2.UserResponse.FromString,
                _registered_method=True)
        self.UpdateUser = channel.unary_unary(
                '/DSBDService/UpdateUser',
                request_serializer=dsbd__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=dsbd__pb2.UserResponse.FromString,
                _registered_method=True)
        self.DeleteUser = channel.unary_unary(
                '/DSBDService/DeleteUser',
                request_serializer=dsbd__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=dsbd__pb2.UserResponse.FromString,
                _registered_method=True)
        self.GetTickerValue = channel.unary_unary(
                '/DSBDService/GetTickerValue',
                request_serializer=dsbd__pb2.GetTickerRequest.SerializeToString,
                response_deserializer=dsbd__pb2.TickerResponse.FromString,
                _registered_method=True)
        self.GetTickerAverage = channel.unary_unary(
                '/DSBDService/GetTickerAverage',
                request_serializer=dsbd__pb2.GetTickerAverageRequest.SerializeToString,
                response_deserializer=dsbd__pb2.TickerResponse.FromString,
                _registered_method=True)
        self.UpdateUserThresholds = channel.unary_unary(
                '/DSBDService/UpdateUserThresholds',
                request_serializer=dsbd__pb2.UpdateUserThresholdsRequest.SerializeToString,
                response_deserializer=dsbd__pb2.UserResponse.FromString,
                _registered_method=True)
        self.ResetUserThresholds = channel.unary_unary(
                '/DSBDService/ResetUserThresholds',
                request_serializer=dsbd__pb2.ResetUserThresholdsRequest.SerializeToString,
                response_deserializer=dsbd__pb2.UserResponse.FromString,
                _registered_method=True)


class DSBDServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LoginUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTickerValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTickerAverage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserThresholds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetUserThresholds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DSBDServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoginUser': grpc.unary_unary_rpc_method_handler(
                    servicer.LoginUser,
                    request_deserializer=dsbd__pb2.LoginUserRequest.FromString,
                    response_serializer=dsbd__pb2.UserResponse.SerializeToString,
            ),
            'RegisterUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterUser,
                    request_deserializer=dsbd__pb2.RegisterUserRequest.FromString,
                    response_serializer=dsbd__pb2.UserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=dsbd__pb2.UpdateUserRequest.FromString,
                    response_serializer=dsbd__pb2.UserResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=dsbd__pb2.DeleteUserRequest.FromString,
                    response_serializer=dsbd__pb2.UserResponse.SerializeToString,
            ),
            'GetTickerValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTickerValue,
                    request_deserializer=dsbd__pb2.GetTickerRequest.FromString,
                    response_serializer=dsbd__pb2.TickerResponse.SerializeToString,
            ),
            'GetTickerAverage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTickerAverage,
                    request_deserializer=dsbd__pb2.GetTickerAverageRequest.FromString,
                    response_serializer=dsbd__pb2.TickerResponse.SerializeToString,
            ),
            'UpdateUserThresholds': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserThresholds,
                    request_deserializer=dsbd__pb2.UpdateUserThresholdsRequest.FromString,
                    response_serializer=dsbd__pb2.UserResponse.SerializeToString,
            ),
            'ResetUserThresholds': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetUserThresholds,
                    request_deserializer=dsbd__pb2.ResetUserThresholdsRequest.FromString,
                    response_serializer=dsbd__pb2.UserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DSBDService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('DSBDService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DSBDService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LoginUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/DSBDService/LoginUser',
            dsbd__pb2.LoginUserRequest.SerializeToString,
            dsbd__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RegisterUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/DSBDService/RegisterUser',
            dsbd__pb2.RegisterUserRequest.SerializeToString,
            dsbd__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/DSBDService/UpdateUser',
            dsbd__pb2.UpdateUserRequest.SerializeToString,
            dsbd__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/DSBDService/DeleteUser',
            dsbd__pb2.DeleteUserRequest.SerializeToString,
            dsbd__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTickerValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/DSBDService/GetTickerValue',
            dsbd__pb2.GetTickerRequest.SerializeToString,
            dsbd__pb2.TickerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTickerAverage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/DSBDService/GetTickerAverage',
            dsbd__pb2.GetTickerAverageRequest.SerializeToString,
            dsbd__pb2.TickerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateUserThresholds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/DSBDService/UpdateUserThresholds',
            dsbd__pb2.UpdateUserThresholdsRequest.SerializeToString,
            dsbd__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ResetUserThresholds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/DSBDService/ResetUserThresholds',
            dsbd__pb2.ResetUserThresholdsRequest.SerializeToString,
            dsbd__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
