import json
import pandas as pd
from kafka import KafkaConsumer
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load model & scaler
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

consumer = KafkaConsumer(
    "swift-transactions",
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print(" Listening to SWIFT transactions from Kafka...\n")

for message in consumer:
    txn_data = message.value
    df_txn = pd.DataFrame([txn_data])
    features = df_txn.drop(['label'], axis=1, errors='ignore')
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)[0]
    status = "🚨 FRAUDULENT" if prediction == 1 else "✅ NORMAL"
    print(f"[RECEIVED] ₹{txn_data.get('amount', 0):.2f} | Location: {txn_data.get('location', 'Unknown')} ➤ {status}")
