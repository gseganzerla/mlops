from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({'model': 'classification'})


if __name__ == '__main__':
    app.run('0.0.0.0', 5001)