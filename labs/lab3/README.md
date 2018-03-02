### How to Setup

```sh
virtualenv -p python3 my-venv
. my-venv/bin/activate
pip3 install -r requirements.txt
```

### How to run Chat server

```sh
python3 server.py
```

### How to run a Chat client

```sh
python3 client.py [username]
```

__Expected Output__

# Bob's client
```sh
python3 client.py Bob
User[Bob] Connected to the chat server.
[Bob] > 
[Alice]: Hi from Alice.
[Smith]: Hi from Smith.
[Bob] > Hello World
```

# Alice's client
```sh
python3 client.py Bob
User[Alice] Connected to the chat server. 
[Alice] > Hi from Alice.
[Smith]: Hi from Smith.
[Bob]: Hello World
```