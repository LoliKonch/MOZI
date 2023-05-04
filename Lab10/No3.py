def solve(a, p):
    x1 = pow(a, int(((p + 1) / 4)), p)
    x2 = pow(-1*a, int(((p + 1) / 4)), p)
    if x1 == x2:
        return x1, -x2
    else:
        return 'решения нет'

a = 5
p = 31
print(pow(25, 2, p))
print(solve(a, p))