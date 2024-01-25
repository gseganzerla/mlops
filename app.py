from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/classification")
def classification():
    response = requests.get('http://127.0.0.1:5001').json()
    return response

@app.route("/regression")
def regression():
    response = requests.get('http://127.0.0.1:5002').json()
    return response


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)