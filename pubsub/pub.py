import time

import redis_client

client = redis_client.get_client()

while True:
    print('Publishing message...')
    message = 'Hello from pub!'
    client.publish(redis_client.TEST_CHANNEL, message)
    time.sleep(1)
