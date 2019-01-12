# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

input_int = int(input('Введите число:\n'))
left = 0

for i in range(1, input_int + 1):
    left += i
else:
    right = int(input_int * (input_int + 1) / 2)

    if left == right:
        print(f'левая часть {left} == правая часть {right}')
    else:
        print(f'левая часть {left} != правая часть {right}')
