# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.


from collections import Counter


def find_count_substr(str):
    """
    Вот что значит прокачался на питоне =) функцию сразу реализовал, но помучался с тем чтоб правильно подстроки выбирать
    это уже говорит что голова устала =)
    Если убрать hash() тогда можно будет посмотреть какие подстроки сколько раз встречаются
    """
    counter_substr = Counter()
    for i, char in enumerate(str):
        j = 0
        length = len(str)
        while j < length-i:
            if length == i+j+1 and i == 0:
                j += 1
                continue

            index = str[i:i+j+1]
            # print(f'str[{i}:{i+j+1}] :{index}')
            counter_substr[index] += 1
            j += 1
    return counter_substr


# str = input("Введите текст:")
str = 'mama'
print(find_count_substr(str))


