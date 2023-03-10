def binary_NOD(num1, num2):
    shift = 0
    print(num1, num2)

    while (num1 | num2) & 1 == 0:
        shift += 1
        num1 >>= 1
        num2 >>= 1

    print(shift, num1, num2)

    while num1 != 0:

        while num1 & 1 == 0:
            num1 >>= 1

        while num2 & 1 == 0:
            num2 >>= 1

        print(num1, num2)

        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1

        print(num1, num2)

    return num2 << shift

a = 5949114
b = 3941396
print(binary_NOD(a, b))

#лол я прогнал тесты и по итогу бинарный дольше, но говорят на  плюсах он быстрее