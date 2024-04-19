
import redis_client

client = redis_client.get_client()

channel = redis_client.TEST_CHANNEL
pubsub = client.pubsub()
pubsub.subscribe(channel)

print(f'Subscribed to {channel}. Waiting for messages...')

for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Received: {message['data'].decode('utf-8')}")
