from Lab7 import Prepare_No12
import random


for n in Prepare_No12.throwMeSomeNumbers():
    k = [random.randint(2, n - 2) for i in range(5)]
    number = n - 1
    s = 0
    t = 0

    while True:
        if number % 2 == 0:
            s += 1
            number /= 2
        else:
            t =  int(number)
            break

    for i in k:
        flag = False
        for r in range(s):
            x = pow(i, (2 ** r) * t, n)

            if  x == 1 or x == n - 1:
                flag = True
                break
        if not flag:
            break



    if flag:
        print(n, "Прошло тест, вероятность простоты ", 1 - 1 / 4 ** len(k))
    else:
        print(n, "Не прошло тест")