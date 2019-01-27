# import cProfile

def findByEratosphen(n):
    if n == 1 or n < 1:
        return 2

    size = n*n
    sieve = [i for i in range(size)]

    sieve[1] = 0
    for i in range(2, size):
        if sieve[i] != 0:
            j = i + i
            while j < size:
                sieve[j] = 0
                j += i

    result = [v for v in sieve if v != 0]
    return result[n-1]


print(findByEratosphen(100))

# 100 loops, best of 3: 25.2 usec per loop - 10
# 100 loops, best of 3: 101 usec per loop - 20
# 100 loops, best of 3: 3.05 msec per loop - 100
# 100 loops, best of 3: 14.5 msec per loop - 200
# 100 loops, best of 3: 51.8 msec per loop - 300

"""
cProfile.run('findByEratosphen(100)')
6 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task2.py:18(<listcomp>)
        1    0.004    0.004    0.006    0.006 task2.py:3(findByEratosphen)
        1    0.001    0.001    0.001    0.001 task2.py:8(<listcomp>)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def findSimpleNumbers(n):
    s_nums = []
    i = 1
    while len(s_nums) < n:
        i += 1
        if i > 10 and i % 10 == 5:
            continue

        for e in s_nums:
            if e * e - 1 > i:
                s_nums.append(i)
                break
            if i % e == 0:
                break
        else:
            s_nums.append(i)

    return s_nums[n-1]
# 100 loops, best of 3: 10.8 usec per loop - 10
# 100 loops, best of 3: 28.3 usec per loop - 20
# 100 loops, best of 3: 251 usec per loop - 100
# 100 loops, best of 3: 615 usec per loop - 200
# 100 loops, best of 3: 1.05 msec per loop - 300

"""
cProfile.run('findSimpleNumbers(100)')
645 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task2.py:43(findSimpleNumbers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

def findByEratosphenv2(n):
    if n == 1:
        return 2

    ar = n*n
    a = list(range(ar + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= ar:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, ar + 1, i):
                a[j] = 0
        i += 1

    return lst[n-1]
# 100 loops, best of 3: 31.7 usec per loop - 10
# 100 loops, best of 3: 114 usec per loop - 20
# 100 loops, best of 3: 2.9 msec per loop - 100
# 100 loops, best of 3: 14.4 msec per loop - 200
# 100 loops, best of 3: 38.5 msec per loop - 300

"""
cProfile.run('findByEratosphenv2(100)')
1233 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.004    0.004    0.004    0.004 task2.py:82(findByEratosphenv2)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

