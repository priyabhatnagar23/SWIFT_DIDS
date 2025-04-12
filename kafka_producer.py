import json
import time
import pandas as pd
from kafka import KafkaProducer

df = pd.read_csv("simulated_swift_data.csv")

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Sending simulated transactions to Kafka topic 'swift-transactions'...\n")

for i in range(20):
    txn = df.sample(1).drop(['timestamp', 'sender', 'receiver'], axis=1)
    txn_data = txn.to_dict(orient='records')[0]
    producer.send("swift-transactions", txn_data)
    print(f"[SENT] {txn_data}")
    time.sleep(1)

producer.flush()
producer.close()
