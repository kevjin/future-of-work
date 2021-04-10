import redis

r = redis.Redis(host='localhost', port=6379, db=0)
n=4000 #how many record/keys should the db be keeping track of
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

def insert_stroke(stroke,color=1):
    # expected input: a stroke comprised of a list of segments
    # color, space for rgb of the stroke
    # each segment is represented by x1,y1,x2,y2 to represent a segment from (x1,y1) to (x2,y2)
    # i.e.[[675, 200, 673, 200], [673, 200, 669, 206], [669, 206, 657, 222]]
    success=True
    for seg in stroke: 
        key=str(seg)
        key=key[1:-1]#remove the [] before after the string, i.e. "673, 200, 669, 206"
        success=set_data(key,color)
        if not success:
            return "error occurred in inserting to database"
    return "stroke recorded"

