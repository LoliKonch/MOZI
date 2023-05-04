import numpy as np


def polyPerf(n):
    n = bin(n - 1)[2:]
    n = ('0' * (4 - len(n))) + n
    n = list(n)
    return n


def polyMult(n1, n2):
    preResult = []
    result = []
    for i in range(3, -1, -1):
        for k in range(3, -1, -1):
            if n1[i] == '1' and n2[k] == '1':
                preResult.append(6 - i - k)

    for i in range(17):
        if preResult.count(i) % 2 == 1:
            result.append(i)
    return result


def polyDiv(n1, n2):
    n = [0 for i in range(8)]
    ndiv = [0 for i in range(8)]
    for i in n1:
        n[7 - i] = 1
    for i in range(8):
        if n[0] == 0:
            n.pop(0)
        else:
            break

    for i in n2:
        ndiv[7 - i] = 1
    for i in range(8):
        if ndiv[0] == 0:
            ndiv.pop(0)
        else:
            break

    return np.polydiv(n, ndiv)


def magikGlue(i, k):
    strin = ''
    chto, kto = polyDiv(polyMult(polyPerf(i), polyPerf(k)), [4, 1, 0])
    kto = list(kto)
    for i in range(len(kto)):
        if i == 0:
            kto[i] = 0
        else:
            kto[i] = 1
    for el in kto:
        strin += str(el)
    kto = int(strin, base=2)
    return kto


table = [['' for k in range(17)] for i in range(17)]
table[0][0] = 0

for i in range(17):
    if i > 0:
        table[0][i] = i - 1

for i in range(17):
    if i > 0:
        table[i][0] = i - 1

for i in range(1, 17):
    for k in range(1, 17):
        if i == 1 or k ==1:
            table[i][k] = 0
        else:
            table[i][k] = magikGlue(i, k)

print(np.matrix(table))



