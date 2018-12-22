# Пользователь вводит две буквы.
# Определить, на каких местах алфавита
# они стоят и сколько между ними находится букв.
import string

chars = input('Введите через пробел две буквы: \n')
chars = chars.split(' ')

if (not chars[0].isnumeric()) and (not chars[1].isnumeric()):

    a = str(chars[0]).lower()
    b = str(chars[1]).lower()

    indexA = string.ascii_lowercase.index(a)
    indexB = string.ascii_lowercase.index(b)
    array = sorted([indexA, indexB])

    print(f'\nБуква {a} находится на {indexA+1} месте\nБуква {b} находится на {indexB+1} месте.')
    print(f'\nРазница между ними {(int(array[1]) - int(array[0]))-1} буквы')
else:
    print('Вы ввели не корректные данные, попробуйте снова')
