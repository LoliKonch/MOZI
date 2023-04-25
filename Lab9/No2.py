def chineze_theo (modn1, modn2, modn3, n1, n2, n3):
    M = n1 * n2 * n3
    M1 = n2 * n3
    M2 = n1 * n3
    M3 = n1 * n2

    r1 = pow(M1, -1, n1)
    r2 = pow(M2, -1, n2)
    r3 = pow(M3, -1, n3)

    answer = (M1 * r1 * modn1 + M2 * r2 * modn2 + M3 * r3 * modn3) % M

    return answer

n1 = 3
n2 = 7
n3 = 5
modn1 = 2
modn2 = 3
modn3 = 0

print(chineze_theo(modn1, modn2, modn3, n1, n2, n3))