#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

# not declaring a queue name causes RabbitMQ to give us a random one.
# The ``exclusive`` flag causes the queue to be deleted upon disconnect.
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print 'Waiting...'

def callback(ch, method, properties, body):
    print '[X] {!r}'.format(body)

channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
