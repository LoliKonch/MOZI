def ostfinder (n, n1, n2, n3):
    ostlist = []
    max = n1 * n2 * n3
    for i in range(1, max + 1):
        ostlist.append(i % n)
    return ostlist

def solutionfinder (modn1, modn2, modn3, n1, n2, n3):
    ostlist1 = ostfinder(n1, n1, n2, n3)
    ostlist2 = ostfinder(n2, n1, n2, n3)
    ostlist3 = ostfinder(n3, n1, n2, n3)

    for i in range(len(ostlist1)):
        if ostlist1[i] == modn1 and ostlist2[i] == modn2 and ostlist3[i] == modn3:
            return i + 1


n1 = 3
n2 = 5
n3 = 7
modn1 = 2
modn2 = 3
modn3 = 4

print(solutionfinder(modn1, modn2, modn3, n1, n2, n3))