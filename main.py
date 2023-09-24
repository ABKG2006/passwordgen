from pwgen import passgen
lenght=int(input("Şifre ne kadar uzun olsun?\n"))
runCount=int(input("Kaç tane şifre istiyorsunuz?\n"))
for i in range(runCount):
    print(passgen(lenght)+"\n")