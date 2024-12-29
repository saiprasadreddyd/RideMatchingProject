import logging
from kafka import KafkaConsumer, KafkaProducer
import json
import pg8000.native

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# PostgreSQL connection setup
db_connection = pg8000.native.Connection(
    user="postgres",
    password="password123",
    database="ride_matching",
    host="localhost",
    port=5432
)

# Kafka setup
consumer = KafkaConsumer(
    "driver_locations",
    "rider_requests",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def match_rides():
    for message in consumer:
        logging.info(f"Processing message: {message.value}")
        if message.topic == "driver_locations":
            driver = message.value
            # Save driver location to DB
            db_connection.run("INSERT INTO drivers (driver_id, location) VALUES (:id, :loc)", 
                              id=driver["driver_id"], loc=driver["location"])
        elif message.topic == "rider_requests":
            rider = message.value
            # Match rider with a driver and send match
            ride_match = {"rider_id": rider["rider_id"], "driver_id": 1}  # Simplified logic
            producer.send("ride_matches", ride_match)
            logging.info(f"Produced ride match: {ride_match}")

if __name__ == "__main__":
    match_rides()
