import random
def passgen(l):
    chars="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password=""
    for i in range(l):
        password+=random.choice(chars)
    
    return password
