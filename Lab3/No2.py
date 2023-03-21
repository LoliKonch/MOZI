def binary_NOD(num1, num2):
    shift = 0
    a, d = 1, 1
    b, c = 0, 0

    while (num1 | num2) & 1 == 0:
        shift += 1
        num1 >>= 1
        num2 >>= 1
    x = num1
    y = num2

    while x != 0:
        while x & 1 == 0:
            x >>= 1
            if (a | b) & 1 == 0:
                a >>= 1
                b >>= 1
            else:
                a += num2
                b -= num1
                a >>= 1
                b >>= 1


        while y & 1 == 0:
            y >>= 1
            if (c | d) & 1 == 0:
                c >>= 1
                d >>= 1
            else:
                c += num2
                d -= num1
                c >>= 1
                d >>= 1

        if x >= y:
            x -= y
            a -= c
            b -= d
        else:
            y -= x
            c -= a
            d -= b

    return y << shift, c, d

A = 5949114
B = 3941396
print(binary_NOD(A, B))