# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10

array1 = list(random.randint(2000, 3000) for _ in range(0, SIZE))
print(array1)

min_element_index = 0
min_element = len(array1)
max_element_index = 0
max_element = 0
current_index = 0

for element in array1:
    if min_element > element:
        min_element = element
        min_element_index = current_index

    if max_element < element:
        max_element = element
        max_element_index = current_index

    current_index += 1

array1[min_element_index], array1[max_element_index] = max_element, min_element
print(array1)
