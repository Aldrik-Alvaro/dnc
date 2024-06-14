import hashlib
def create_hashid(key_string):
    return hashlib.md5(key_string.encode()).hexdigest()