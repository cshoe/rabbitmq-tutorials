#!/usr/bin/env pika
import random
import time

import pika


def callback(ch, method, properties, body):
    print " [X] Received {!r}".format(body)
    time.sleep(random.randint(1,10))
    print ' [X] Done'
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')
print ' [*] Waiting for messages. To exit press CTRL + C'
channel.start_consuming()
