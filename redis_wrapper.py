import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def set_data(key, value):
    success=r.set(key, value)
    return success

def get_data(key):
    res=r.get(key)
    return res
