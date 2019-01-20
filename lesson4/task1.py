# import cProfile
import random


def func1(size):
    array = list(random.randint(0, size * size) for _ in range(0, size))
    min_element_index = 0
    min_element = max(array)
    max_element_index = 0
    max_element = min(array)

    for i, element in enumerate(array):
        if min_element > element:
            min_element = element
            min_element_index = i

        if max_element < element:
            max_element = element
            max_element_index = i

    if min_element_index > max_element_index:
        array = array[max_element_index + 1:min_element_index]
    else:
        array = array[min_element_index + 1:max_element_index]

    return sum(array)
# 100 loops, best of 3: 17.4 usec per loop - 10
# 100 loops, best of 3: 32 usec per loop - 20
# 100 loops, best of 3: 150 usec per loop  - 100
# 100 loops, best of 3: 301 usec per loop  - 200
# 100 loops, best of 3: 1.49 msec per loop - 1 000
# 100 loops, best of 3: 2.98 msec per loop - 2 000
# 100 loops, best of 3: 14.9 msec per loop - 10 000
# 100 loops, best of 3: 30 msec per loop   - 20 000
# 100 loops, best of 3: 159 msec per loop - 100 000
# 100 loops, best of 3: 305 msec per loop - 200 000
# 10 loops, best of 3: 1.5 sec per loop - 1 000 000

"""
cProfile.run('func1(100)')
665 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 task1.py:5(func1)
      101    0.000    0.000    0.000    0.000 task1.py:6(<genexpr>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      157    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

def func2(size):
    array = list(random.randint(0, size * size) for _ in range(0, size))
    min_index = array.index(min(array))
    max_index = array.index(max(array))

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    return sum(array[min_index+1:max_index])
# 100 loops, best of 3: 17.4 usec per loop - 10
# 100 loops, best of 3: 149 usec per loop - 100
# 100 loops, best of 3: 149 msec per loop - 100 000
# 10 loops, best of 3: 1.49 sec per loop - 1 000 000

"""
cProfile.run('func2(100)')
667 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.001    0.001 task1.py:61(func2)
      101    0.000    0.000    0.001    0.000 task1.py:62(<genexpr>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      157    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""


def func3(size):
    array = [random.randint(0, size * size) for _ in range(size)]

    idx_min = 0
    idx_max = 0
    for i in range(1, len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    if idx_min > idx_max:
        idx_min, idx_max = idx_max, idx_min

    summ = 0
    for i in range(idx_min + 1, idx_max):
        summ += array[i]

    return summ
# 100 loops, best of 3: 16.6 usec per loop - 10
# 100 loops, best of 3: 151 usec per loop - 100
# 100 loops, best of 3: 298 usec per loop - 200
# 100 loops, best of 3: 157 msec per loop - 100 000
# 100 loops, best of 3: 308 msec per loop - 200 000
# 10 loops, best of 3: 1.53 sec per loop - 1 000 000

"""
cProfile.run('func3(100)')
572 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 task1.py:100(<listcomp>)
        1    0.000    0.000    0.000    0.000 task1.py:99(func3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      166    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""


def func4(size):
    array = [random.randint(0, size * size) for _ in range(size)]
    (_, max_index) = max((val, i) for i, val in enumerate(array))
    (_, min_index) = min((val, i) for i, val in enumerate(array))

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    return sum(array[min_index+1:max_index])
# 100 loops, best of 3: 19 usec per loop - 10
# 100 loops, best of 3: 165 usec per loop - 100
# 100 loops, best of 3: 169 msec per loop - 100 000
# 10 loops, best of 3: 1.68 sec per loop - 1 000 000

"""
cProfile.run('func4(100)')
776 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 task1.py:146(func4)
        1    0.000    0.000    0.000    0.000 task1.py:147(<listcomp>)
      101    0.000    0.000    0.000    0.000 task1.py:148(<genexpr>)
      101    0.000    0.000    0.000    0.000 task1.py:149(<genexpr>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      166    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

# array = [2527, 2599, 2023, 2204, 2559, 2463, 2864, 2401, 2407, 2414]
# assert func3(10) == 7226