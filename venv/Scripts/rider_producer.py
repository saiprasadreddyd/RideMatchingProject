import json
import logging
from kafka import KafkaProducer # type: ignore

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("RiderProducer")

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce_ride_requests():
    try:
        logger.info("Producing ride requests...")
        ride_requests = [
            {"rider_id": 101, "location": {"lat": 40.7128, "lon": -74.0060}},
            {"rider_id": 102, "location": {"lat": 41.8781, "lon": -87.6298}},
        ]
        for request in ride_requests:
            producer.send('ride_requests', request)
            logger.info(f"Sent ride request: {request}")
    except Exception as e:
        logger.error(f"Error producing ride requests: {e}")

if __name__ == "__main__":
    produce_ride_requests()
