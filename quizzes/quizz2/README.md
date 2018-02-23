### How to Setup

```sh
virtualenv my-venv
. my-venv/bin/activate
pip3 install -r requirements.txt
```

### How to run?
```sh
FLASK_APP=hello.py flask run
```

### GET /

```sh
curl -i http://127.0.0.1:5000/
```

### POST users

```sh
curl -i -X POST http://127.0.0.1:5000/users -d "name=foo"
```