def NOD_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = NOD_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x

a = 5949114
b = 3941396
print(NOD_extended(a, b))
(1234, 1786351, -2696305)