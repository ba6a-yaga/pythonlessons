# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

SIZE = 10

array1 = list(random.randint(-100, 100) for _ in range(0, SIZE))
print(array1)

min_value = 0
min_value_key = 0

for k, v in enumerate(array1):
    print(v)
    if min_value > v:
        min_value = v
        min_value_key = k
else:
    print(f'Максимальное отрицательное значение {min_value} находится на {min_value_key} индексе массива')