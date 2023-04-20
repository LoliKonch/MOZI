from Prepare_No12 import throwMeSomeNumbers as th

k = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def NOD_recursion(num1, num2):
    if num1 == 0:
        return num2
    return NOD_recursion(num2 % num1, num1)

for n in th():
    flag = True

    for i in k:
        if NOD_recursion(i, n) != 1:
            flag = False
            break
    else:
        for i in k:
            if pow(i, n - 1, n) != 1:
                flag = False

    if flag:
        print(n, "Прошло тест")
    else:
        print(n, "Не прошло тест")


