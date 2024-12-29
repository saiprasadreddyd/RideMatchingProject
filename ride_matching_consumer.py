import logging
from kafka import KafkaConsumer
import json

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Kafka Consumer setup
consumer = KafkaConsumer(
    "ride_matches",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

def consume_ride_matches():
    for message in consumer:
        logging.info(f"Received ride match: {message.value}")

if __name__ == "__main__":
    consume_ride_matches()
