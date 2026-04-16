import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

print("Loading dataset...")
df = pd.read_csv("data/creditcard.csv")

print("Preparing features and target...")
X = df.drop("Class", axis=1)
y = df["Class"]

print("Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Scaling data...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

print("Training model...")
model = RandomForestClassifier(
    n_estimators=20,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)
model.fit(X_train_scaled, y_train)

print("Saving files...")
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/fraud_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Model and scaler saved successfully.")