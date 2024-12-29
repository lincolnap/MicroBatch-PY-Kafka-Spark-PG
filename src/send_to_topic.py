from faker import Faker
from kafka import KafkaProducer
import json
import time

# Crear instancia de Faker
faker = Faker()

# Configurar Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9094',  # Cambia por tu servidor de Kafka
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Nombre del topic de Kafka
kafka_topic = 'test'  # Cambia por el nombre de tu topic

def generate_fake_data():
    """Genera datos falsos usando Faker."""
    return {
        "name": faker.name(),
        "location": faker.city(),
        "phone": faker.phone_number()
    }

def send_to_kafka():
    """Genera datos y los envía al producer de Kafka."""
    while True:
        data = generate_fake_data()
        print(f"Enviando: {data}")
        producer.send(kafka_topic, value=data)
        time.sleep(2)  # Envía un mensaje cada segundo

if __name__ == "__main__":
    try:
        send_to_kafka()
    except KeyboardInterrupt:
        print("Proceso detenido por el usuario.")
    finally:
        producer.close()
