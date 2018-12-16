# Написать программу, которая генерирует в указанных пользователем границах:
#  - случайное целое число;
#  - случайное вещественное число;
#  - случайный символ.
# Для каждого из трех случаев пользователь задает свои границы
# диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести
# на экран любой символ алфавита от 'a' до 'f' включительно.
import string
import random

range = input('Введите через пробле диапазон - два целых/вещественных числа или два символа латинского алфавита: \n')
range = range.split(' ')

# В процессе создания блок схемы я указал проверку на тип через type,
# оно конечно логично что type строки отдает строку, но я думал у питона внутри есть какая то
# реализация которая определяет. В итоге погуглив увидел такую интересную проверку, а блок схему не стал изменять
if (not range[0].isdigit()) and (not range[0].replace('.', '', int(range[0][0])).isdigit()):
    a = str(range[0]).lower()
    b = str(range[1]).lower()
    range = sorted(range)

    indexA = string.ascii_lowercase.index(a)
    indexB = string.ascii_lowercase.index(b)

    array = sorted([indexA, indexB])
    rand = random.randrange(int(array[0]), int(array[1]))
    r = string.ascii_lowercase[rand]

    print(f'Случайное в диапазоне {str(range[0]).upper()} и {str(range[1]).upper()} : {r.upper()}')
elif range[0].isdigit():
    array = sorted([range[0], range[1]])
    r = random.randrange(int(array[0]), int(array[1]))

    print(f'Случайное в диапазоне {array[0]} и {array[1]} : {r}')
elif range[0].replace('.', '', int(range[0][0])).isdigit():
    array = sorted([range[0], range[1]])
    r = random.uniform(float(array[0]), float(array[1]))

    print(f'Случайное в диапазоне {range[0]} и {range[1]} : {round(r,1)}')
else:
    print('Вы ввели не корректные данные, попробуйте снова')
