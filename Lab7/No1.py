import math as m
from Prepare_No12 import throwMeSomeNumbers as th

def perebor(number):
    for i in range(2, int(m.sqrt(number)) - 1):
        if number % i == 0:
            return False
    return True


for i in th():
    if perebor(i):
        print(i, "Простое")
    else:
        print(i, "Не простое")