import pika
import json
import os
import time

def connect():
    """Tenta se conectar ao RabbitMQ com retry."""
    params = pika.ConnectionParameters(
        host=os.getenv("RABBITMQ_HOST", "rabbitmq"),
        credentials=pika.PlainCredentials(
            os.getenv("RABBITMQ_USER", "user"),
            os.getenv("RABBITMQ_PASS", "password")
        )
    )
    while True:
        try:
            connection = pika.BlockingConnection(params)
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("Aguardando RabbitMQ subir...")
            time.sleep(5)

def send_message(message: dict):
    connection = connect()
    channel = connection.channel()
    channel.queue_declare(queue="mensagens", durable=True)

    channel.basic_publish(
        exchange="",
        routing_key="mensagens",
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)
    )

    print(f"Mensagem enviada: {message}")
    connection.close()
