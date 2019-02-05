# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
array = [round(random.uniform(0.0, 50.0), 2) for i in range(0, 10)]

# ar_1 = [2, 10, 15, 5, 12, 6]

# [15]
# left = [2, 10, 5, 12, 6]
# right = []
# --> [2, 10, 5, 12, 6][15]
# [5]
# left = [2]
# right = [10, 12, 6]
# --> [2][5][10, 12, 6][15]
# [12]
# left = [10, 6]
# right = []
# --> [2][5][10, 6][12][15]
# [10]
# left = [6]
# right = []
# --> [2][5][6][10][12][15]


def sorted_by_merge(array: list):
    """
    Выше представил последовательные действия с массивом, как я понял по описанию сортировку слияния, но когда подошел к
    return я увидел что могу использовать из урока возврат как в быстрой сортировки. Честно не понял отличия быстрой сортировки
    и слияния. И там и там разбивается массив сначала до одного элемента, так как один элемент в массиве считается отсортированным.
    """
    def split_array(array: list):
        if len(array) <= 1:
            return array

        left = []
        right = []
        rand_index = random.randint(0, len(array) - 1)
        rand_element = array[rand_index]
        array.pop(rand_index)

        for item in array:
            if item >= rand_element:
                right.append(item)
            else:
                left.append(item)

        # print(f'--> {left} {[rand_element]} {right}')
        return split_array(left) + [rand_element] + split_array(right)
    return split_array(array)



print(f' Исходный массив:{array}')
array = sorted_by_merge(array)
print(f' Отсортированный массив:{array}')
