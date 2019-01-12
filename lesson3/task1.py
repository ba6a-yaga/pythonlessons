#  В диапазоне натуральных чисел от 2 до 99 определить,
#  сколько из них кратны любому из чисел в диапазоне от 2 до 9.

list1 = range(2, 9)
list2 = range(2, 99)

for l1 in list1:
    multiples = list()
    for l2 in list2:
        if l2 % l1 == 0:
            multiples.append(l2)
    else:
        print(f'Для числа {l1} было найдено {multiples.__len__()} кратных чисел - {multiples}')
