def NOD_recursion(num1, num2):
    if num1 == 0:
        return num2
    print(f'{num1} = {num2} * {num1//num2} + {num2%num1}')
    return NOD_recursion(num2 % num1, num1)

a = 5949114
b = 3941396
print(a, b)
print(NOD_recursion(a, b))