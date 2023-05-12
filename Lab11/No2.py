import numpy as np

def createIndexTable (a, p):
    indexMatchN = [pow(a, i, p) for i in range(p - 1)]
    nMatchindex = [[0, 0] for i in range(p - 1)]
    for i in range(1, p):
        nMatchindex[i - 1][0] = i
        try:
            nMatchindex[i - 1][1] = indexMatchN.index(i)
        except:
            nMatchindex[i - 1][1] = None

    return np.matrix(nMatchindex)


a = 7
p = 27

print(createIndexTable(a, p))