def binary_NOD(num1, num2):
    shift = 0
    a = d = 1
    b = c = 0

    while (num1 | num2) & 1 == 0:
        shift += 1
        num1 >>= 1
        num2 >>= 1
    x = num1
    y = num2

    while num1 != 0:
        while num1 & 1 == 0:
            num1 >>= 1
            if (a | b) & 1 == 0:
                a >>= 1
                b >>= 1
            else:
                a += y
                b -= x
                a >>= 1
                b >>= 1


        while num2 & 1 == 0:
            num2 >>= 1
            if (c | d) & 1 == 0:
                c >>= 1
                d >>= 1
            else:
                c += y
                d -= x
                c >>= 1
                d >>= 1

        if num1 >= num2:
            num1 -= num2
            a -= c
            b -= d
        else:
            num2 -= num1
            c -= a
            d -= b

    return num2 << shift, c, d

A = 5949114
B = 3941396
print(binary_NOD(A, B))