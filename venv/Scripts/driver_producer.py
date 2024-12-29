import json
import logging
from kafka import KafkaProducer 

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DriverProducer")

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce_driver_locations():
    try:
        logger.info("Producing driver location updates...")
        drivers = [
            {"driver_id": 1, "location": {"lat": 37.7749, "lon": -122.4194}},
            {"driver_id": 2, "location": {"lat": 34.0522, "lon": -118.2437}},
        ]
        for driver in drivers:
            producer.send('driver_locations', driver)
            logger.info(f"Sent driver location: {driver}")
    except Exception as e:
        logger.error(f"Error producing driver locations: {e}")

if __name__ == "__main__":
    produce_driver_locations()
