from functools import wraps
import json

def to_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return json.dumps(f(*args, **kwargs))
    
    return wrapper

@to_json
def get_data():
    return {'data':42}

print(get_data())