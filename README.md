**Ride Matching Project**

This project implements a ride-matching system using Apache Kafka, PostgreSQL, and Python. The system consists of producers and consumers for simulating drivers, riders,
and ride-matching services, all while utilizing a robust Kafka-based architecture.

**Features**

Driver Producer: Simulates driver location updates.
Rider Producer: Simulates ride requests from riders.
Ride Matching Service: Matches riders to nearby drivers.
Database Integration: PostgreSQL for persisting ride-related data.
Logging: Provides detailed logs for debugging and monitoring.

**Technologies Used**

Apache Kafka: For messaging and streaming data.
PostgreSQL: As the database for persisting driver and rider information.
Python: For implementing producers, consumers, and the ride-matching service.
Docker: For containerized deployment of Kafka, ZooKeeper, and PostgreSQL.

**Setup Instructions**

1. Prerequisites
Install Docker and Docker Compose.
Install Python 3.10+.
Install Git.
2. Clone the Repository
git clone https://github.com/saiprasadreddyd/RideMatchingProject.git
cd RideMatchingProject
3. Install Python Dependencies
Create a virtual environment and install the required libraries:
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
4. Start Services with Docker
Use Docker Compose to start ZooKeeper, Kafka, and PostgreSQL:
docker-compose up -d
Verify:
Kafka: Running on localhost:9092.
PostgreSQL: Accessible on localhost:5432 (user: postgres, password: password123).
5. Run Python Scripts
Run the Python scripts in separate terminals:
python driver_producer.py
python rider_producer.py
python ride_matching_service.py
python ride_matching_consumer.py

**How It Works**
Driver Producer:
Sends simulated driver location updates to a Kafka topic.

Rider Producer:
Sends simulated ride requests to a Kafka topic.

Ride Matching Service:
Consumes messages from the driver and rider topics.
Matches riders with nearby drivers.
Saves match data to PostgreSQL.

Ride Matching Consumer:
Logs ride matches from the Kafka topic.

**Project Structure**
RideMatchingProject/
│
├── driver_producer.py         # Driver producer script
├── rider_producer.py          # Rider producer script
├── ride_matching_service.py   # Ride-matching service
├── ride_matching_consumer.py  # Consumer for ride matches
├── docker-compose.yml         # Docker setup for Kafka, ZooKeeper, PostgreSQL
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation

**Future Enhancements**
Add real-time web interface to visualize rides.
Implement advanced ride-matching algorithms.
Add fault tolerance and scalability features.
Contributors
Sai Prasad Reddy D
