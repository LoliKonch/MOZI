import numpy as np


def polyPerf(n):
    n = bin(n - 1)[2:]
    n = list(n)
    return n


def polyMult(n1, n2):
    preResult = []
    result = []
    for i in range(len(n1)):
        for k in range(len(n2)):
            if n1[i] == '1' and n2[k] == '1':
                preResult.append(len(n1) + len(n2) - 2 - i - k)

    for i in range(N - 1):
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

[1,0,0,0,1]
def showPoly(ost):
    for i in range(len(ost)):
        if ost[i] == 1:
            print(f'{"1" if len(ost) - i - 1 == 0 else f"x{dictExp[len(ost) - i - 1]}"}'
                  f'{"+" if ost[i + 1:].count(1) != 0 else ""}', end='')
    print('')


def magikGlue(i, k, choose):
    tempString = ''
    # тут в "polyDiv(polyMult(polyPerf(i), polyPerf(k)), [4, 1, 0])" часть [4, 1, 0] это представление полинома
    # по которому необходимо привести  в данном случае я взял Х**4 + Х**1(просто Х) + Х**0(просто 1)
    # и ты просто в этот список все степени Х из полинома переносишь и всё готово дальше само
    cel, ost = polyDiv(polyMult(polyPerf(i), polyPerf(k)), [4, 1, 0])
    ost = list(ost)
    for i in range(len(ost)):
        if ost[i] == 1 or ost[i] == -1:
            ost[i] = 1
        else:
            ost[i] = 0

    if choose == k - 1:
        showPoly(ost)

    for elem in ost:
        tempString += str(elem)
    ost= int(tempString, base=2)
    return ost

dictExp = {
    0: "\u2070",
    1: "\u00B9",
    2: "\u00B2",
    3: "\u00B3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079"
    }
# N - это размерность таблицы обязательно бери степени двойки типо 4 8 16 и тд
N = 16
# choose - это "элемент" из 3 столбца таблицы
choose = 10
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
            table[i][k] = magikGlue(i, k, choose)



#print(polyDiv(polyMult(polyPerf(5 + 1), polyPerf(7 + 1)), [3, 1, 0]))
#print(np.polydiv([1, 1, 0, 1, 1], [1, 0, 1, 1]))
#print(magikGlue(7 + 1, 5 + 1))
print(np.matrix(table))