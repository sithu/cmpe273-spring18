import zmq
import sys

# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

# Send a "message" using the socket
msg = " ".join(sys.argv[1:])
print("[client]:" + msg)
sock.send_string(msg)

msg = sock.recv()
print("[received]:" + msg.decode())