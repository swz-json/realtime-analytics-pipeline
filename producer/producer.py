import os
from kafka import KafkaProducer
import json, time, random

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    data = {
        "transaction_id": random.randint(1, 100000),
        "amount": round(random.uniform(10, 500), 2),
        "city": random.choice(["Paris", "Nice", "Lyon"]),
        "timestamp": time.time()
        "timestamp": time.time()
    }
    producer.send("transactions", value=data)
    print("Sent:", data)
    time.sleep(1)
