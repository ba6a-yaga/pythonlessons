# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 50

array1 = list(random.randint(1, 10) for _ in range(0, SIZE))
print(array1)
dict1 = dict()

for i in array1:
    if dict1.get(i).__bool__():
        dict1[i] += 1
    else:
        dict1[i] = 1
else:
    max_value = 0
    key = ''
    for k in dict1.keys():
        if max_value < dict1[k]:
            max_value = dict1[k]
            key = k
    print(dict1)
    print(f'Число {key} встречается в массиве {max_value} раз')