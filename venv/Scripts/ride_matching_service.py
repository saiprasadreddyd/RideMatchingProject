import json
import logging
from kafka import KafkaConsumer, KafkaProducer
import pg8000

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("RideMatchingService")

# Kafka configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
consumer = KafkaConsumer(
    'ride_requests',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# PostgreSQL configuration
DB_CONFIG = {
    "user": "postgres",
    "password": "Welcome@123",
    "database": "ride_matching",
    "host": "localhost",
    "port": 5432
}

def connect_to_db():
    try:
        conn = pg8000.connect(**DB_CONFIG)
        logger.info("Connected to PostgreSQL database.")
        return conn
    except Exception as e:
        logger.error(f"Error connecting to the database: {e}")
        return None

def match_rides():
    conn = connect_to_db()
    if not conn:
        return

    try:
        logger.info("Matching rides...")
        for message in consumer:
            ride_request = message.value
            logger.info(f"Processing ride request: {ride_request}")
            
            # Perform matching logic (example: match with first available driver)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM drivers LIMIT 1;")
            driver = cursor.fetchone()

            if driver:
                match = {"rider": ride_request, "driver": driver}
                producer.send('matched_rides', match)
                logger.info(f"Matched ride: {match}")
    except Exception as e:
        logger.error(f"Error in ride matching service: {e}")
    finally:
        conn.close()
        logger.info("Database connection closed.")

if __name__ == "__main__":
    match_rides()
