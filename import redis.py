import redis

# Connection to Redis
redis_host = 'localhost'  # Change this if your Redis server is on a different host
redis_port = 6379
redis_db = 0

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

# Store (key, value) pair
key = 'my_key'
value = 'my_value'
redis_client.set(key, value)

# Search for a key
search_key = 'my_key'
retrieved_value = redis_client.get(search_key)

if retrieved_value:
    print(f"Value for key '{search_key}': {retrieved_value.decode('utf-8')}")
else:
    print(f"Key '{search_key}' not found.")
