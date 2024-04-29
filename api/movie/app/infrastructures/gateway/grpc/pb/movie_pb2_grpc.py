# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

from . import movie_pb2 as movie__pb2


class MovieServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetByIds = channel.unary_stream(
            "/movie_service.MovieService/GetByIds",
            request_serializer=movie__pb2.GetByIdsRequest.SerializeToString,
            response_deserializer=movie__pb2.Movie.FromString,
        )
        self.GetById = channel.unary_unary(
            "/movie_service.MovieService/GetById",
            request_serializer=movie__pb2.GetByIdRequest.SerializeToString,
            response_deserializer=movie__pb2.Movie.FromString,
        )


class MovieServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetByIds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MovieServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetByIds": grpc.unary_stream_rpc_method_handler(
            servicer.GetByIds,
            request_deserializer=movie__pb2.GetByIdsRequest.FromString,
            response_serializer=movie__pb2.Movie.SerializeToString,
        ),
        "GetById": grpc.unary_unary_rpc_method_handler(
            servicer.GetById,
            request_deserializer=movie__pb2.GetByIdRequest.FromString,
            response_serializer=movie__pb2.Movie.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "movie_service.MovieService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class MovieService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetByIds(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/movie_service.MovieService/GetByIds",
            movie__pb2.GetByIdsRequest.SerializeToString,
            movie__pb2.Movie.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetById(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/movie_service.MovieService/GetById",
            movie__pb2.GetByIdRequest.SerializeToString,
            movie__pb2.Movie.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )