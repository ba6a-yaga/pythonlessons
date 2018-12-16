# Найти сумму и произведение цифр
# трехзначного числа, которое вводит пользователь.

threeDigit = input('Введите трехзначное целое число: ')
length = threeDigit.__len__()

if length == 3:
    customSum = int(threeDigit[0])+int(threeDigit[1])+int(threeDigit[2])
    customProduct = int(threeDigit[0])*int(threeDigit[1])*int(threeDigit[2])
    print(f'Сумма трехзначного числа {threeDigit} = {customSum}\nПроизведение трехзначного числа {threeDigit} = {customProduct}')
else:
    print(f'Вы ввели {length}-хзначное, а нужно трехзначное число, попробуйте снова')
