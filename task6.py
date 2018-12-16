# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.
import string

num = input('Введите номер буквы: \n')

if num.isnumeric():
    if int(num) > string.ascii_uppercase.__len__():
        print(f'Букв в алфавите {string.ascii_uppercase.__len__()}, попробуйте снова')
    else:
        ch = string.ascii_uppercase[int(num)-1]

        print(f'Вы ввели букву {ch}')
else:
    print('Вы ввели не корректные данные, попробуйте снова')
