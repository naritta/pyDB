# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import put_pb2 as put__pb2


class DBStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Put = channel.unary_unary(
        '/put.DB/Put',
        request_serializer=put__pb2.PutRequest.SerializeToString,
        response_deserializer=put__pb2.PutResponse.FromString,
        )


class DBServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Put(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DBServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Put': grpc.unary_unary_rpc_method_handler(
          servicer.Put,
          request_deserializer=put__pb2.PutRequest.FromString,
          response_serializer=put__pb2.PutResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'put.DB', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
