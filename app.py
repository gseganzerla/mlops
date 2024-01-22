from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/classification")
def hello():
    return requests.get('http://127.0.0.1:5001').json()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)