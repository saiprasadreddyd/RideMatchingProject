import logging
from kafka import KafkaProducer
import json
import time

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Kafka Producer setup
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def produce_rider_requests():
    riders = [
        {"rider_id": 101, "location": "Location A", "destination": "Location C"},
        {"rider_id": 102, "location": "Location B", "destination": "Location D"},
    ]
    for rider in riders:
        logging.info(f"Sending rider data: {rider}")
        producer.send("rider_requests", rider)
        time.sleep(2)

if __name__ == "__main__":
    produce_rider_requests()
