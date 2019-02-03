# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random
array = [random.randint(-100, 100) for i in range(0, 10)]
print(f' Исходный массив:{array}')


def sorted_by_bubble(array):
    ar = []
    for order_desc in range(len(array)-1, 0, -1):
        if ar == array:
            return array
        ar = array.copy()
        for i in range(order_desc):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


sorted_by_bubble(array)
print(f' Отсортированный массив:{array}')

