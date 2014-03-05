#!/usr/bin/env python
import sys

import pika


"""
Pretty much the same thing as ``send.py`` except we're making the queue
durable and messages persistent.
"""

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def publish(message):
    channel.basic_publish(exchange='', routing_key='task_queue', body=message,
        properties=pika.BasicProperties(delivery_mode=2))
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
