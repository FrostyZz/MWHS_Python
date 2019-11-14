import random

num = int(input("How long do you want your password to be? \n"))

def pwGen(num):
    i = random.randrange(0,3)
    password = ""
    for i in range(0,num):
        j = random.randrange(0,3)
        if j == 0:
            j = random.randrange(65,91) # lower
            password+=chr(j)
        elif j == 1:
            j = random.randrange(97,123) # upper
            password+=chr(j)
        else: 
            j = random.randrange(48,58) # nums
            password+=chr(j)
    return password

pwGen(num)
print(pwGen(num))