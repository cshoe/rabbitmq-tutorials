#!/usr/bin/env pika
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def publish(message):
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print " [X] Sent '{!r}'".format(message)

if __name__ == '__main__':
    publish('First Message')
    publish('Second Message')
    publish('Third Message')
    publish('Fourth Message')
    publish('Fifth Message')
    publish('Sixth Messgae')
    publish('Seventh Message')
    connection.close()
