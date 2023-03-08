def NOD_recursion(num1, num2):
    if num1 == 0:
        return num2
    print(num1, "=", num2, "*", num1//num2, "+", num2%num1)
    return NOD_recursion(num2 % num1, num1)

A = 3941396
B = 5949114
print(A, B)
print(NOD_recursion(A, B))