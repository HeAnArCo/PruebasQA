from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import uuid

# Crear el consumidor
consumer = KafkaConsumer(
    'gps-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Esperando mensajes de 'gps-topic'...\n")

# Leer mensajes infinitamente
for message in consumer:
    print("Mensaje recibido:")
    print(message.value)


# Crear el productor
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simular mensaje GPS
mensaje = {
    "id": str(uuid.uuid4()),
    "lat": 4.7110,
    "lon": -74.0721,
    "speed": 72
}

# Enviar mensaje
producer.send('gps-topic', mensaje)
producer.flush()
print("Mensaje enviado:", mensaje)