import math

def firstCheck(n):
    for i in range(2, 25):
        if n % i == 0:
            return int(n / i), i
    return n, 1

def factorizeFerma(n):

    n, i = firstCheck(n)

    x = int(math.sqrt(n))
    if x**2 == n:
        return x, x, i
    else:
        x += 1
    while True:
        if x == (n + 1) / 2:
            return n, i
        else:
            y = int(math.sqrt(x**2 - n))

        if y**2 == x**2 - n:
            return x + y, x - y, i
        else:
            x += 1

n = int(input())
print(factorizeFerma(n))