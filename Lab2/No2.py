def binary_NOD(num1, num2):
    shift = 0

    while (num1 | num2) & 1 == 0:
        shift += 1
        num1 >>= 1
        num2 >>= 1

    while num1 & 1 == 0:
        num1 >>= 1
    while num2 != 0:
        while num2 & 1 == 0:
            num2 >>= 1
        if num1 > num2:
            num1, num2 = num2, num1
        num2 -= num1
    return num1 << shift

a = 5949114
b = 3941396
print(binary_NOD(a, b))

#лол я прогнал тесты и по итогу бинарный дольше, но говорят на  плюсах он быстрее