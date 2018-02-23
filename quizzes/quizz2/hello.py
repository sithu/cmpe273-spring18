from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def new_users():
    name = request.form["name"]
    return "Hello {}!".format(name)
