#нахождение n-ого простого числа c помощью алгоритма решето Эратосфена
import cProfile
def simple_1(n):
    a = [0] * n
    for i in range(n):
        a[i] = i

    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
         if a[i] != 0:
             b.append(a[i])
    del a
    return b
'''Время выполнения через timeit'''
#python -m timeit -n 100 -s "import simple_1" "simple_1.simple_1(11)" 100 loops, best of 3: 2.6 usec per loop
#python -m timeit -n 100 -s "import simple_1" "simple_1.simple_1(111)"100 loops, best of 3: 26.9 usec per loop
#python -m timeit -n 100 -s "import simple_1" "simple_1.simple_1(1111)"100 loops, best of 3: 332 usec per loop


#cProfile.run('simple_1(10000)')

'''
         1233 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.004    0.004    0.004    0.004 simple_1.py:3(simple_1)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

#cProfile.run('simple_1(1000)')

'''
         172 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 simple_1.py:3(simple_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
