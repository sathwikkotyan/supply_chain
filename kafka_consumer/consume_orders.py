from confluent_kafka import Consumer
import json, time, pandas as pd
from datetime import datetime
import os

conf = {
    "bootstrap.servers": "pkc-921jm.us-east-2.aws.confluent.cloud:9092",
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "PLAIN",
    "sasl.username": "GBJML63ME2TILJTK",
    "sasl.password": "cfltMfled8GKafzq94uLlab+3+eg+3SjZLAx06TTr0EKuT9HTk3lRpEw7keZVPxQ",
    "group.id": f"supplychain-batch-{int(time.time())}",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": False
}

consumer = Consumer(conf)
consumer.subscribe(["supply_chain_orders"])

records = []
end_time = time.time() + 10   # poll for 10 seconds

while time.time() < end_time:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        continue
    records.append(json.loads(msg.value().decode("utf-8")))

consumer.close()

print("Records:", len(records))

if not records:
    raise Exception("No records consumed")

df = pd.DataFrame(records)

os.makedirs("data/bronze", exist_ok=True)
path = f"data/bronze/orders_{datetime.now().strftime('%Y%m%d_%H%M%S')}.parquet"
df.to_parquet(path, index=False)

print("Saved batch to", path)
