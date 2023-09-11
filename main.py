import random

validChars="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght=int(input("Şifre ne kadar uzun olsun?\n"))
runCount=int(input("Kaç tane şifre istiyorsunuz?\n"))
for i in range(runCount):
    password=""
    for j in range(lenght):
        nextChar=random.choice(validChars)
        while(password!="" and nextChar==password[-1]):
            nextChar=random.choice(validChars)
        password+=nextChar
    print(password+"\n")

