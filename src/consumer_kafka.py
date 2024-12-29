from kafka import KafkaConsumer,TopicPartition
from secrets import secrets
import psycopg2
import json
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    database="streaming", 
    user=f'{os.getenv("POSTGRES_USER")}', 
    password=f'{os.getenv("POSTGRES_PASSWORD")}', 
    host="localhost", 
    port=5432
    )

# Create the Kafka consumer
consumer = KafkaConsumer(
    bootstrap_servers='localhost:9094',
    group_id='my-ramdom-data',
    enable_auto_commit=True,
    auto_offset_reset='earliest'
)

con_db = conn.cursor()

# Assign partitions manually
consumer.assign([TopicPartition('test', 0)])  # Assign to partition 0

# Seek to a specific offset (e.g., start reading from offset 100)
#consumer.seek(TopicPartition('test', 0), 100)

# Consume messages
for message in consumer:
    msg = json.loads(message.value.decode('utf-8'))
    print(msg['name'] + msg['location'] + msg['phone'])
    consumer.commit()
    con_db.execute("""INSERT INTO clients (name, location, phone) 
                      VALUES (%s,%s,%s);""",
                      (msg['name'],msg['location'], msg['phone']))
    conn.commit()
    print("Transaction committed successfully!")
    print(f"Insert message: {msg}")


con_db.close()
conn.close()