import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

# Run a simple "Echo" server
while True:
    message = sock.recv()
    message = message.decode()
    message = message[::-1]
    sock.send_string("Echo: " + message)
    print("[Server] Echo: " + message)