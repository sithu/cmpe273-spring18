## Requirements

You will be building a drone dancing simulator in Python using GRPC as a communication protocol.

![](https://usatftw.files.wordpress.com/2018/02/drones.jpg)

The simulator has two components:
- Server
- Client

### Server

The server is the main orchestrator to guide directions for all drone in the network. The role of server are:
- Drone/client membership
- Getting user inputs for the whole drone cluster movement.
- Sending new coordinate to each drone.

#### 1. Membership

New drone will join to the server.


### Client

Each drone will act as a client which will be listening commands from the server.