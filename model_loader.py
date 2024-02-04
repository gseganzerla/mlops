import pandas as pd
import joblib

def model_loader(data, model_type):
    df = pd.DataFrame([data])
    model = joblib.load(f'propensao_inadimplencia_{model_type}.joblib')

    return model, df