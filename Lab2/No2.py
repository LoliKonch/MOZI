def binary_gcd(num1, num2):
    shift = 0

    while (num1 | num2) & 1 == 0:
        shift += 1
        num1 >>= 1
        num2 >>= 1
    print(shift, num1, num2)

    while num1 & 1 == 0:
        num1 >>= 1
    print(shift, num1, num2)

    while num2 != 0:
        while num2 & 1 == 0:
            num2 >>= 1

        if num1 > num2:
            num1, num2 = num2, num1

        num2 -= num1
    print(shift, num1, num2)

    return num1 << shift

a = 2829188
b = 1682388
print(binary_gcd(a, b))