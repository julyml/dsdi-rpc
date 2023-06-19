# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_analise_pb2 as grpc__analise__pb2


class MensageiroStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EnviarMensagemVazia = channel.unary_unary(
                '/mensageiro.Mensageiro/EnviarMensagemVazia',
                request_serializer=grpc__analise__pb2.Resposta_Request_Void.SerializeToString,
                response_deserializer=grpc__analise__pb2.Resposta_Request_Void.FromString,
                )
        self.EnviarMensagemLong = channel.unary_unary(
                '/mensageiro.Mensageiro/EnviarMensagemLong',
                request_serializer=grpc__analise__pb2.Resposta_Request_Long.SerializeToString,
                response_deserializer=grpc__analise__pb2.Resposta_Request_Long.FromString,
                )
        self.EnviarMensagemOitoLong = channel.unary_unary(
                '/mensageiro.Mensageiro/EnviarMensagemOitoLong',
                request_serializer=grpc__analise__pb2.Resposta_Request_Long.SerializeToString,
                response_deserializer=grpc__analise__pb2.Resposta_Request_Long.FromString,
                )
        self.EnviarMensagemString = channel.unary_unary(
                '/mensageiro.Mensageiro/EnviarMensagemString',
                request_serializer=grpc__analise__pb2.Resposta_Request_String.SerializeToString,
                response_deserializer=grpc__analise__pb2.Resposta_Request_String.FromString,
                )


class MensageiroServicer(object):
    """The greeting service definition.
    """

    def EnviarMensagemVazia(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnviarMensagemLong(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnviarMensagemOitoLong(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnviarMensagemString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MensageiroServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EnviarMensagemVazia': grpc.unary_unary_rpc_method_handler(
                    servicer.EnviarMensagemVazia,
                    request_deserializer=grpc__analise__pb2.Resposta_Request_Void.FromString,
                    response_serializer=grpc__analise__pb2.Resposta_Request_Void.SerializeToString,
            ),
            'EnviarMensagemLong': grpc.unary_unary_rpc_method_handler(
                    servicer.EnviarMensagemLong,
                    request_deserializer=grpc__analise__pb2.Resposta_Request_Long.FromString,
                    response_serializer=grpc__analise__pb2.Resposta_Request_Long.SerializeToString,
            ),
            'EnviarMensagemOitoLong': grpc.unary_unary_rpc_method_handler(
                    servicer.EnviarMensagemOitoLong,
                    request_deserializer=grpc__analise__pb2.Resposta_Request_Long.FromString,
                    response_serializer=grpc__analise__pb2.Resposta_Request_Long.SerializeToString,
            ),
            'EnviarMensagemString': grpc.unary_unary_rpc_method_handler(
                    servicer.EnviarMensagemString,
                    request_deserializer=grpc__analise__pb2.Resposta_Request_String.FromString,
                    response_serializer=grpc__analise__pb2.Resposta_Request_String.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mensageiro.Mensageiro', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mensageiro(object):
    """The greeting service definition.
    """

    @staticmethod
    def EnviarMensagemVazia(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mensageiro.Mensageiro/EnviarMensagemVazia',
            grpc__analise__pb2.Resposta_Request_Void.SerializeToString,
            grpc__analise__pb2.Resposta_Request_Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnviarMensagemLong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mensageiro.Mensageiro/EnviarMensagemLong',
            grpc__analise__pb2.Resposta_Request_Long.SerializeToString,
            grpc__analise__pb2.Resposta_Request_Long.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnviarMensagemOitoLong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mensageiro.Mensageiro/EnviarMensagemOitoLong',
            grpc__analise__pb2.Resposta_Request_Long.SerializeToString,
            grpc__analise__pb2.Resposta_Request_Long.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnviarMensagemString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mensageiro.Mensageiro/EnviarMensagemString',
            grpc__analise__pb2.Resposta_Request_String.SerializeToString,
            grpc__analise__pb2.Resposta_Request_String.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)