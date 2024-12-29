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

def produce_driver_locations():
    drivers = [
        {"driver_id": 1, "location": "Location A"},
        {"driver_id": 2, "location": "Location B"},
    ]
    for driver in drivers:
        logging.info(f"Sending driver data: {driver}")
        producer.send("driver_locations", driver)
        time.sleep(2)

if __name__ == "__main__":
    produce_driver_locations()
