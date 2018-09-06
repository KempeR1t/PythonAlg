_author_= 'Швец Александр Николаевич'
#Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
import cProfile
def task_1(n):
    a = [[random.randint(0,100) for _ in range (n)] for x in range(n)]

    c=[]

    for x in range(len(a)):
        min_el = [row[x] for row in a][0]
        for z in range(len([row[x] for row in a])):
            if [row[x] for row in a][z] < min_el:
                min_el = [row[x] for row in a][z]
        c.append(min_el)

    for x in c:
        if x > min_el:
            min_el = x
    return min_el


'''Время выполнения через timeit'''
# 50 loops, best of 3: 49.2 msec per loop - для массива 100х100
# 50 loops, best of 3: 4.09 msec per loop - для массива 40х40
# 50 loops, best of 3: 330 msec per loop - для массива 200х200

#cProfile.run('task_1(100)')
'''
         63536 function calls in 0.055 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.058    0.058 <string>:1(<module>)
    10000    0.006    0.000    0.013    0.000 random.py:173(randrange)
    10000    0.003    0.000    0.016    0.000 random.py:217(randint)
    10000    0.005    0.000    0.007    0.000 random.py:223(_randbelow)
      100    0.000    0.000    0.000    0.000 zadacha_itog_1.py:12(<listcomp>)
      100    0.000    0.000    0.000    0.000 zadacha_itog_1.py:13(<listcomp>)
    10000    0.033    0.000    0.033    0.000 zadacha_itog_1.py:14(<listcomp>)
      383    0.001    0.000    0.001    0.000 zadacha_itog_1.py:15(<listcomp>)
        1    0.004    0.004    0.058    0.058 zadacha_itog_1.py:6(task_1)
        1    0.000    0.000    0.019    0.019 zadacha_itog_1.py:7(<listcomp>)
        1    0.000    0.000    0.058    0.058 {built-in method builtins.exec}
      101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12747    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

#cProfile.run('task_1(30)')
'''
         5890 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
      900    0.001    0.000    0.001    0.000 random.py:173(randrange)
      900    0.000    0.000    0.001    0.000 random.py:217(randint)
      900    0.000    0.000    0.001    0.000 random.py:223(_randbelow)
       30    0.000    0.000    0.000    0.000 zadacha_itog_1.py:12(<listcomp>)
       30    0.000    0.000    0.000    0.000 zadacha_itog_1.py:13(<listcomp>)
      900    0.001    0.000    0.001    0.000 zadacha_itog_1.py:14(<listcomp>)
       96    0.000    0.000    0.000    0.000 zadacha_itog_1.py:15(<listcomp>)
        1    0.000    0.000    0.003    0.003 zadacha_itog_1.py:6(task_1)
        1    0.000    0.000    0.001    0.001 zadacha_itog_1.py:7(<listcomp>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
       31    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       30    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      900    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1168    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''



#В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

def minimum(b):
    min_el = b[0]
    min_ind = 0
    for x in range(len(b)):
        if b[x] < min_el:
            min_el = b[x]
            min_ind = x
    return min_el, min_ind

def task_2(n):
    a = [random.randint(0,100) for _ in range (n)]
    a.pop(minimum(a)[1])
    return minimum(a)[0]

'''Время выполнения через timeit'''
# 100 loops, best of 3: 54.8 usec per loop - для n 50
# 100 loops, best of 3: 5.53 msec per loop - для n 5000
# 100 loops, best of 3: 11.1 msec per loop - для n 10000

#cProfile.run('task_2(50)')
'''
         277 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       50    0.000    0.000    0.000    0.000 random.py:173(randrange)
       50    0.000    0.000    0.000    0.000 random.py:217(randint)
       50    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
        1    0.000    0.000    0.000    0.000 test.py:15(task_2)
        1    0.000    0.000    0.000    0.000 test.py:16(<listcomp>)
        2    0.000    0.000    0.000    0.000 test.py:6(minimum)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       50    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       67    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
'''

#cProfile.run('task_2(5000)')
'''
         26302 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
     5000    0.003    0.000    0.006    0.000 random.py:173(randrange)
     5000    0.001    0.000    0.007    0.000 random.py:217(randint)
     5000    0.002    0.000    0.003    0.000 random.py:223(_randbelow)
        1    0.000    0.000    0.008    0.008 test.py:15(task_2)
        1    0.001    0.001    0.008    0.008 test.py:16(<listcomp>)
        2    0.000    0.000    0.000    0.000 test.py:6(minimum)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     5000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     6292    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
'''

#cProfile.run('task_2(10000)')
'''
         52723 function calls in 0.018 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.018    0.018 <string>:1(<module>)
    10000    0.006    0.000    0.013    0.000 random.py:173(randrange)
    10000    0.002    0.000    0.015    0.000 random.py:217(randint)
    10000    0.004    0.000    0.006    0.000 random.py:223(_randbelow)
        1    0.000    0.000    0.018    0.018 test.py:15(task_2)
        1    0.002    0.002    0.017    0.017 test.py:16(<listcomp>)
        2    0.001    0.000    0.001    0.000 test.py:6(minimum)
        1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12713    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
'''



#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

def task_3(n):
    a = [random.randint(0,100) for _ in range (n)]

    max_el, min_el = a[0], a[0]
    max_ind , min_ind = 0, 0

    for x in range(len(a)):
        if a[x] > max_el:
            max_el = a[x]
            max_ind = x
        if a[x] < min_el:
            min_el = a[x]
            min_ind = x

    summa = 0

    if max_ind < min_ind:
        max_ind , min_ind = min_ind, max_ind
    for x in range(min_ind+1,max_ind):
            summa += a[x]
    return summa

'''Время выполнения через timeit'''
# 100 loops, best of 3: 53.8 usec per loop - для n 50
# 100 loops, best of 3: 559 usec per loop - для n 500
# 100 loops, best of 3: 5.39 msec per loop - для n 5000

#cProfile.run("task_3(50)")
'''
         273 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       50    0.000    0.000    0.000    0.000 random.py:173(randrange)
       50    0.000    0.000    0.000    0.000 random.py:217(randint)
       50    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
        1    0.000    0.000    0.000    0.000 test.py:7(task_3)
        1    0.000    0.000    0.000    0.000 test.py:8(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       50    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       67    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

#cProfile.run("task_3(500)")
'''
         2645 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
      500    0.000    0.000    0.001    0.000 random.py:173(randrange)
      500    0.000    0.000    0.001    0.000 random.py:217(randint)
      500    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
        1    0.000    0.000    0.001    0.001 test.py:7(task_3)
        1    0.000    0.000    0.001    0.001 test.py:8(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      639    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

#cProfile.run("task_3(5000)")
'''
         26341 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
     5000    0.003    0.000    0.006    0.000 random.py:173(randrange)
     5000    0.001    0.000    0.008    0.000 random.py:217(randint)
     5000    0.002    0.000    0.003    0.000 random.py:223(_randbelow)
        1    0.000    0.000    0.009    0.009 test.py:7(task_3)
        1    0.001    0.001    0.009    0.009 test.py:8(<listcomp>)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     5000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     6335    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
'''