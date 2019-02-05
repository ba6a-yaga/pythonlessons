# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random, math
from collections import deque
# array = [5, 2, 1, 8, 10, 3, 6]
# array = [6, 5, 1, 8, 10] #6
# array = [2, 5, 1, 8, 10] #5
# array = [2, 5, 1, 8, 10, 3, 6]
# array = [5, 2, 1]
array = [random.randint(1, 1000) for i in range(10)]
print(array)

# array = [2, 10, 15, 5, 12, 6]
# --> 2 5 6 10 12 15
# 2
# 2 10
# 2 10 15
# 5 10 15
# 5 10 12
# 6 10 12

# array = [2, 5, 1, 8, 10, 3, 6]
#  --> 1 2 3 5 6 8 10
# 2
# 2 5
# 1 2 5
# 2 5 8
# 5 8 10
# 3 5 8
# 3 5 6


def get_median(array):
    """
    Начинал я с гугла и поиска примеров-ориентиров и это моя третья реализация, вторая получилось на основе быстрой
    сортировки. Первая реализация представлена ниже get_median_1. В любом случае все три реализации они не решают задачу.
    Очень близки +- один элемент в массива. Текущая функция очень перегружена условиями но я ее сохранил так как была идея
    - реализовать с помощью двухсторонней очереди нахождение среднего элемента, конечно тут можно ее упростить и привести
    в порядок, но потратил много времени и решил оставить так для показа.
    """
    queue = deque([array[0]], maxlen=3)

    def diff_left(l, m, item):
        if l <= item and m >= item:
            return [m]+[item]
        if l > item:
            return [l]+[item]

    def diff_right(r, m, item):
        if r >= item and m <= item:
            return [m]+[item]
        if r < item:
            return [r]+[item]

    for i, item in enumerate(array):
        if i == 0:
            continue

        print(f' [start] {i} --> {list(queue)}')

        if queue[0] >= item:
            queue.appendleft(item)
            continue
        elif queue[len(queue) - 1] <= item:
            queue.append(item)
            continue

        if len(queue) < 2:
            if queue[0] > item:
                left = diff_left(0, queue[0], item)
                print(f'left: {left}')
                queue.appendleft(left[1])
            else:
                right = diff_right(0, queue[0], item)
                print(f'right: {right}')
                queue.append(right[1])
        else:
            if queue[1] >= item:
                left = diff_left(queue[0], queue[1], item)
                print(f'left: {left}')
                if len(queue) > 2:
                    queue.rotate(-2)
                    queue.extendleft(left)
                else:
                    queue.appendleft(left[1])
                    if queue[1] < left[1]:
                        queue[0], queue[1] = queue[1], queue[0]
            else:
                if len(queue) > 2:
                    right = diff_right(queue[2], queue[1], item)
                    print(f'right: {right}')
                    queue.rotate(2)
                    queue.extend(right)
                else:
                    right = diff_right(0, queue[1], item)
                    print(f'right: {right}')
                    queue.append(right[1])
                    if queue[1] > right[1]:
                        queue[1], queue[2] = queue[2], queue[1]
        print(f'  {i} --> {list(queue)}')


    return queue[1]


# def get_median_1(array):
#     """
#     Это та функция которую на гуглил и может слегка переделал, самая первая реализация, она не решает так же задачу, и я
#     ее закомментировал
#     """
#     length = len(array)
#     if length < 1:
#         return
#
#     if length % 2 == 0:
#         m = (array[length // 2 - 1: length // 2 + 1])
#         return sum(m)//len(m)
#     else:
#         return array[length // 2 - 1]


def get_median_with_sort(array):
    """
    После попыток реализовать без сортировок поиск медианы, реализовал поиск с помощью сортировки
    """
    i = 1
    while i < len(array):
        if not i or array[i - 1] <= array[i]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array[(len(array)-1)//2]


def get_median_gnome_sort_hoffman(array):
    """
    Интересная реализация Питера Хоффмана гномьей сортировки
    """
    pos = 0
    while True:
        if pos == 0:
            pos += 1

        if pos >= len(array):
            break

        if array[pos] >= array[pos - 1]:
            pos += 1
        else:
            array[pos - 1], array[pos] = array[pos], array[pos - 1]
            pos -= 1
    return array[(len(array)-1)//2]

# print(get_median_gnome_sort_hoffman(array))


