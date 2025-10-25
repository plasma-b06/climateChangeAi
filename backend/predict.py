import pandas as pd
import joblib
from utils import decode_risk_label

def predict_risks(input_data):
    df = pd.DataFrame([input_data])

    heat_model = joblib.load("models/heat_model.pkl")
    dengue_model = joblib.load("models/dengue_model.pkl")
    asthma_model = joblib.load("models/asthma_model.pkl")

    heat = decode_risk_label(heat_model.predict(df)[0])
    dengue = decode_risk_label(dengue_model.predict(df)[0])
    asthma = decode_risk_label(asthma_model.predict(df)[0])

    return {
        "heat_risk": heat,
        "dengue_risk": dengue,
        "asthma_risk": asthma
    }
