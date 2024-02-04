from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

default_headers = {'Content-Type': 'application/json'}



@app.route("/classification", methods=['POST'])
def classification():
    data = request.get_json()
    response = requests.post('http://127.0.0.1:5001', json=data, headers=default_headers)

    return response.json()

@app.route("/clusterization", methods=['POST'])
def regression():
    data = request.get_json()
    response = requests.post('http://127.0.0.1:5002', json=data, headers=default_headers)
    return response.json()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)