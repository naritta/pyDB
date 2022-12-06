from concurrent import futures
import grpc
import put_pb2
import put_pb2_grpc

class DB(put_pb2_grpc.DBServicer):
    def Put(self, request, context):
        print("RECV: %s" % request.name)
        message = "Registered, %s!" % request.name
        # todo: make this async and return ASAP
        # todo: use independent Id for filename
        with open("./file.proto", "wb") as fd:
            fd.write(request.SerializeToString())
        print("SEND: %s" % message)
        return put_pb2.PutResponse(message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    put_pb2_grpc.add_DBServicer_to_server(DB(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
