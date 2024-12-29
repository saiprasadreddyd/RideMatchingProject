import json
import logging
from kafka import KafkaConsumer

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("RideMatchingConsumer")

# Kafka consumer configuration
consumer = KafkaConsumer(
    'matched_rides',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_matched_rides():
    try:
        logger.info("Consuming matched rides...")
        for message in consumer:
            ride_match = message.value
            logger.info(f"Received matched ride: {ride_match}")
    except Exception as e:
        logger.error(f"Error consuming matched rides: {e}")

if __name__ == "__main__":
    consume_matched_rides()
