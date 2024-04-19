import os

import redis

TEST_CHANNEL = os.getenv('REDIS_TEST_CHANNEL')

def get_client():
    print(f"connect to redis [{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}]-db{os.getenv('REDIS_DB')} ...")

    return redis.StrictRedis(
        host=os.getenv('REDIS_HOST'), 
        port=int(os.getenv('REDIS_PORT')),
        db=int(os.getenv('REDIS_DB')),
        password=os.getenv('REDIS_PASSWORD'),
   )
