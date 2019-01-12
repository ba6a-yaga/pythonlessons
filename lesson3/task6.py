# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10

array1 = list(random.randint(0, 100) for _ in range(0, SIZE))
print(array1)

min_element_index = 0
min_element = 100
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

if min_element_index > max_element_index:
    print(array1[max_element_index+1:min_element_index])
    print(sum(array1[max_element_index+1:min_element_index]))
else:
    print(array1[min_element_index+1:max_element_index])
    print(sum(array1[min_element_index+1:max_element_index]))
