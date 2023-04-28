def sqrV (p):
    listOst = []
    listV = []
    listnV = []
    for i in range(1, p):
        listOst.append((i**2)%p)

    for i in range(0, p):
        if i in listOst:
            listV.append(i)
        else:
            listnV.append(i)

    return listOst, listV, listnV


num1 = 59
num2 = 67
print(sqrV(num2))
