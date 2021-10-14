import random as rn
size = int(input())
abc = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(_+{:>?{]}[1234567890")
i = 0
password = []
while i < size:
    numabc = rn.randint(0, 80)
    password.append(abc[numabc])
    i+=1
print(*password, sep = "")