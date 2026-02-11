from confluent_kafka import Producer
import pandas as pd
import json
import time

# 1️⃣ Connection details (your login & address)
conf = {
    'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092',  # Post office address
    'security.protocol': 'SASL_SSL',                 # Secure connection
    'sasl.mechanisms': 'PLAIN',                      # Simple login
    'sasl.username': 'GBJML63ME2TILJTK',               # Your username
    'sasl.password': 'cfltMfled8GKafzq94uLlab+3+eg+3SjZLAx06TTr0EKuT9HTk3lRpEw7keZVPxQ'             # Your password
}

producer = Producer(conf)

# 2️⃣ Read your orders data (the letters)
orders = pd.read_csv("../data_generation/orders.csv")

# 3️⃣ Function to check if each message is delivered
def delivery_report(err, msg):
    if err:
        print('❌ Delivery failed:', err)
    else:
        print(f'✅ Sent: {msg.topic()} partition [{msg.partition()}] offset {msg.offset()}')

# 4️⃣ Send each order one by one (like posting letters)
for _, row in orders.iterrows():
    data = row.to_dict()
    producer.produce('supply_chain_orders', value=json.dumps(data), callback=delivery_report)
    producer.poll(0)
    time.sleep(0.05)  # small delay to act like real-time streaming

# 5️⃣ Ensure all messages are sent before closing
producer.flush()
print("🎯 All order data sent to Confluent Kafka!")
