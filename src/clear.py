import redis

db_client = redis.Redis(host='localhost', port=6379, db=0)
for key in db_client.keys():
    db_client.delete(key)
