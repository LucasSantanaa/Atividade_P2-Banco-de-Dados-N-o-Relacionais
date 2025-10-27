import pika
import json
import os
import time

def connect():
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

def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    print(f"Mensagem recebida: {mensagem}")

def main():
    connection = connect()
    channel = connection.channel()
    channel.queue_declare(queue="mensagens", durable=True)
    channel.basic_consume(queue="mensagens", on_message_callback=callback, auto_ack=True)
    print(" Aguardando mensagens...")
    channel.start_consuming()

if __name__ == "__main__":
    main()
