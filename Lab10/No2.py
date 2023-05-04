import math as m


def perebor(number):
    for i in range(2, int(m.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def findSimp (stNum):
    listk1 = []
    listk3 = []
    intervals = {
        1: 100,
        2: 200,
        3: 300,
        0: 400
    }

    startInterval = intervals[stNum%4]

    for i in range(startInterval, startInterval + 100):
        if perebor(i):
            n1 = (i - 1) / 2
            n2 = (i - 3) / 2
            if n1 % 2 == 0 and len(listk1) < 2:
                listk1.append(i)
                continue
            if n2 % 2 == 0 and len(listk3) < 2:
                listk3.append(i)
        if len(listk1) == 2 and len(listk3) == 2:
                break

    return listk1[0], listk1[1], listk3[0], listk3[1]


def legendre(a, p):
    res = pow(int(a), int((p - 1) / 2), int(p))

    if res == p - 1:
        return -1
    if res == 1:
        return 1




def outData (stNum):
    halfList = []
    numList = findSimp(stNum)
    for i in numList:
        n = int(i / 2)
        print(i)
        for ii in range(3,-1, -1):
            print(n - ii, (n - ii)**2, legendre(n - ii, i))

        for ii in range(4):
            print(n + 1 + ii, (n + 1 + ii)**2, legendre(n + 1 + ii, i))


stNum1 = 9
stNum2 = 27

outData(stNum1)