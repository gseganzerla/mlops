from flask import Flask, jsonify, request
import pandas as pd
import joblib
from prediction_returns import classification_return
from model_loader import model_loader

app = Flask(__name__)


@app.route("/", methods=['POST'])
def classification():
    data = request.get_json()
    model, df = model_loader(data, 'classification')
    result = model.predict(df)[0]
    
    return {"model": "classification", 'predictionValue': int(result), 'predictionName': classification_return(result)}


if __name__ == '__main__':
    app.run('0.0.0.0', 5001)