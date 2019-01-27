# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

DICT_HEX = {
        10: 'A', 'A': 10,
        11: 'B', 'B': 11,
        12: 'C', 'C': 12,
        13: 'D', 'D': 13,
        14: 'E', 'E': 14,
        15: 'F', 'F': 15,
    }

calc = {
    '+': lambda dec1, dec2: dec1 + dec2,
    '*': lambda dec1, dec2: dec1 * dec2,
}


def deсimalToHex(number):
    hexNumber = ''
    # print(f'1 - {hexNumber}')
    while number >= 16:
        rem = number % 16
        if rem in DICT_HEX:
            hexNumber += DICT_HEX[rem]
            # print(f'2 - {hexNumber}')
        else:
            hexNumber += str(rem)
            # print(f'3 - {hexNumber}')
        number = number // 16
    if number < 10:
        hexNumber = hexNumber + str(number)
        # print(f'4 - {hexNumber}')
    else:
        hexNumber = hexNumber + DICT_HEX[number]
        # print(f'5 - {hexNumber}')
    hexNumber = list(hexNumber[::-1])
    return hexNumber


def hexToDecimal(x):
    array = list(x[::-1])
    sum_, count = 0, 0
    for i in array:
        if i.isdigit():
            sum_ = sum_ + (int(i) * (16 ** count))
            count += 1
        else:
            # print(array[i])
            # print(DICT_HEX[array[i]])
            # print(f'sum_ = {sum_} + ({int(DICT_HEX[i])} * (16 ** {count}))')
            sum_ = sum_ + (int(DICT_HEX[i]) * (16 ** count))
            count += 1
    return sum_


def main():
    hex1 = list(input('Введите первое шестнадцатиричное число:\n'))
    hex2 = list(input('Введите второе шестнадцатиричное число:\n'))
    op = input('Введите тип операции + или * :\n')

    dec1 = hexToDecimal(hex1)
    dec2 = hexToDecimal(hex2)

    dec = calc[op](dec1, dec2)
    hex = deсimalToHex(dec)

    print(f'{hex1}{op}{hex2} = {hex}')


main()
