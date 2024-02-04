from flask import Flask, jsonify, request
from model_loader import model_loader
from prediction_returns import clusterization_return
import joblib

app = Flask(__name__)


@app.route("/", methods=['POST'])
def clusterization():
    data = request.get_json()

    model, df = model_loader(data, 'clusterization')
    result = model.predict(df)

    clusterization_info = clusterization_return(result)


    return {"model": "clusterization", 'predictionValue': int(result), 'predictionGroup': clusterization_info.get('groupName'), 'averageProbabilityGroup': clusterization_info.get('risk')}


if __name__ == '__main__':
    app.run('0.0.0.0', 5002)