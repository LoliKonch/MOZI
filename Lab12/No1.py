import numpy as np


def polyPerf(n):
    n = bin(n - 1)[2:]
    n = list(n)
    return n


def polyMult(n1, n2):
    preResult = []
    result = []
    for i in range(len(n1) - 1, -1, -1):
        for k in range(len(n2) - 1, -1, -1):
            if n1[i] == '1' and n2[k] == '1':
                preResult.append(len(n1) + len(n2) - 2 - i - k)

    for i in range(N + 1):
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
    tempString = ''
    cel, ost = polyDiv(polyMult(polyPerf(i), polyPerf(k)), [4, 3, 0])
    ost = list(ost)
    for i in range(len(ost)):
        if ost[i] == 0:
            ost[i] = 0
        else:
            ost[i] = 1
    for elem in ost:
        tempString += str(elem)
    ost= int(tempString, base=2)
    return ost


N = 16
table = [['' for k in range(N + 1)] for i in range(N + 1)]
table[0][0] = 0

for i in range(N + 1):
    if i > 0:
        table[0][i] = i - 1

for i in range(N + 1):
    if i > 0:
        table[i][0] = i - 1

for i in range(1, N + 1):
    for k in range(1, N + 1):
        if i == 1 or k ==1:
            table[i][k] = 0
        else:
            table[i][k] = magikGlue(i, k)



#print(polyDiv(polyMult(polyPerf(5), polyPerf(7)), [3, 1, 0]))
#print(np.polydiv([1, 1, 0, 1, 1], [1, 0, 1, 1]))
#print(magikGlue(7, 5))
print(np.matrix(table))