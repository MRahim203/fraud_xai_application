import joblib
import os

model = None
scaler = None

if os.path.exists("models/fraud_model.pkl") and os.path.exists("models/scaler.pkl"):
    model = joblib.load("models/fraud_model.pkl")
    scaler = joblib.load("models/scaler.pkl")


def predict_transaction(input_df):
    if model is None or scaler is None:
        raise RuntimeError("Model or scaler not available.")

    expected_columns = [
        "Time",
        "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
        "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20",
        "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28",
        "Amount"
    ]

    input_df = input_df.copy()

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0.0

    input_df = input_df[expected_columns]

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    return int(prediction), float(probability)