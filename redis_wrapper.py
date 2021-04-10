import redis

r = redis.Redis(host='localhost', port=6379, db=0)
n=10 #how many record/keys should the db be keeping track of
last_n_key=f"last{n}keys"
def set_data(key, value):
    success=r.set(key, value)
    r.lpush(last_n_key,key)
    r.ltrim(last_n_key,0,n-1)
    return success

def get_data(key):
    res=r.get(key)
    return res

def get_last_n(k=n):
    # k need to <=n. Can be used to specify how many would like to actually retrieve
    res=r.lrange(last_n_key,0,k-1)
    return res
