def NOD_recursion(num1, num2):
    if num1 == 0:
        return num2
    print(num1, "=", num2, "*", num1//num2, "+", num2%num1)
    return NOD_recursion(num2 % num1, num1)

a = 2829188
b = 1682388
print(a, b)
print(NOD_recursion(a, b))