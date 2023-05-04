def factorize(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        if n % i != 0:
            print(int(n%i))
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


n = int(input())
print(factorize(n))
