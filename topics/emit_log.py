#!/usr/bin/env python
import sys

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', type='topic')

len_of_args = len(sys.argv)
if len_of_args > 2:
    binding_key = sys.argv[1]
    message = ' '.join(sys.argv[2:])

elif len_of_args == 2:
    binding_key = 'anonymous.info'
    message = ' '.join(sys.argv[1:])
# len of args can never be less than 1
else:
    binding_key = 'anonymous.info'
    message = 'Hello World!'

channel.basic_publish(exchange='topic_logs', routing_key=binding_key, body=message)
print '[X] Sent {!r}:{!r}'.format(binding_key, message)
connection.close()

