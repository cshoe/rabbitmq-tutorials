#!/usr/bin/env python
import sys

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', type='topic')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    print 'need binding keys'
    sys.exit(1)

for key in binding_keys:
    channel.queue_bind(exchange='topic_logs', queue=queue_name,
        routing_key=key)

def callback(ch, method, properties, body):
    print '[X] {!r}'.format(body)

channel.basic_consume(callback, queue=queue_name, no_ack=True)
print 'Waiting...'
channel.start_consuming()

