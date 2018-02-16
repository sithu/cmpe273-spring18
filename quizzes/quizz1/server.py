import time
import grpc
import ping_pb2
import ping_pb2_grpc

from concurrent import futures

class PingServer(ping_pb2.PingPongServicer):
    def ping(self, request, context):
        # TODO
        print("Encode:\n", request)
        return None

def run(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    ping_pb2_grpc.add_PingPongServicer_to_server(PingServer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)
