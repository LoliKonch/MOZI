import math as m


def generateNumber(studentNumber):
    number = (studentNumber + 110) * 23
    numberList1 = []
    numberList2 = []

    for i in range(number - 20, number + 20):
        for ii in range(2, int(m.sqrt(i)) - 1):
            if i % ii == 0:
                break
        else:
            numberList1.append(i)

    for i in range(number - 20, number + 20):
        if i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and not i in numberList1:
            numberList2.append(i)

    return numberList1[0], numberList1[1], numberList2[0], numberList2[1]


def throwMeSomeNumbers():
    numberSet1 = generateNumber(studentNumber1)
    numberSet2 = generateNumber(studentNumber2)
    return numberSet1[0], numberSet1[1], numberSet1[2], numberSet1[3], \
           numberSet2[0], numberSet2[1], numberSet2[2], numberSet2[3], \
           carmicleNumber1, carmicleNumber2


studentNumber1 = 9
studentNumber2 = 27
carmicleNumber1 = 2465
carmicleNumber2 = 2465

numberSet1 = generateNumber(studentNumber1)
numberSet2 = generateNumber(studentNumber2)
