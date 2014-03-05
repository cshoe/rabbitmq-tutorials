#!/usr/bin/env python
import sys

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs', type='direct')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    print 'need severities'
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name,
        routing_key=severity)

def callback(ch, method, properties, body):
    print '[X] {!r}'.format(body)

channel.basic_consume(callback, queue=queue_name, no_ack=True)
print 'Waiting...'
channel.start_consuming()

