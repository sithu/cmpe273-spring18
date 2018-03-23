from flask import Flask

app = Flask(__name__)
MAX_LEN=3

@app.route('/')
def index():
    return 'OK'

# TODO add all routes here!


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)