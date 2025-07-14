# backend/producer.py
from kafka import KafkaProducer
import json
import uuid

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

mensaje = {
    "id": str(uuid.uuid4()),
    "lat": 4.7110,
    "lon": -74.0721,
    "timestamp": "2025-07-13T23:45:00Z"
}

producer.send('TestTopic', mensaje)
producer.flush()
print("Mensaje enviado a Kafka:", mensaje)


#frontend/MapComponent.js