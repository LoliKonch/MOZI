def factorize(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac

def solve(a, p):
    x1 = pow(a, int(((p + 1) / 4)), p)
    x2 = pow(-1*a, int(((p + 1) / 4)), p)
    if x1 == x2:
        return x1, -x2
    else:
        return 'решения нет'

def solveComplicated(a, n):
    listSimple = factorize(n)
    for i in listSimple:
        a1 = a % i
        print(solve(a1, i))

n = 7 * 23
a = 3

solveComplicated(a, n)