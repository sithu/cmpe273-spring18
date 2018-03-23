## Question I

Implement a REST API server that supports a buffer ring data store in server.py.

### Requirements

- [Flask](http://flask.pocoo.org/docs/0.12/quickstart/) for REST API
- [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) for data structure.
- Buffer ring size is 3. (Hint: deque's maxlen = 3)

```
# install Flask if you have not installed it yet.
pip3 install -r requirements.txt

# run the server.
python3 server.py
```

#### 1. POST http://127.0.0.1:3000/items

Append new item to the deque. E.g. deque.append('Alice')

Example:

_Request_

##### HTTP Body
```sh
name=Alice
```

Your solution must work with this below command.

```sh
# Curl Command
curl -d "name=Alice" -X POST http://127.0.0.1:3000/items
```

_Response_

```
201 Created
...
```

> If the deque (ring) is full and a new item is added, the oldest item MUST be discarded from the deque.


#### 2. GET http://127.0.0.1:3000/items

List all items from the deque.

Example:

_Response_

```
200 OK
...


Alice,Bob,Charlie
```

#### 3. GET http://127.0.0.1:3000/items/{index}

Get an item by the index. Assume the index value is greater than -1 and less than the max length.

Example:

_Request_

```sh
GET http://127.0.0.1:3000/items/0
```

_Response_

```
200 OK
...


Alice
```

## Question II

Create a client to the buffer ring REST server from the question I to access its APIs in client.py.

_Expected Output_

```sh
python3 client.py
Chuck
Chuck,Alice,Bob
Alice
Alice,Bob,Charlie
```

## Question III

Port [HRW implementation](https://godoc.org/github.com/codahale/hrw#example-package) from Golang to Python. You can use any Python hash function in hrw.py.

_Expected Output_

```sh
python3 hrw.py
['one.example.com', 'three.example.com', 'five.example.com', 'four.example.com', 'two.example.com', 'six.example.com']
```

> You will get different random order depending on what hash function you use.