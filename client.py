import grpc
import put_pb2
import put_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = put_pb2_grpc.DBStub(channel)
        response = stub.Put(put_pb2.PutRequest(name='key1'))
    print("RECV: %s" % response.message)

if __name__ == '__main__':
    run()
