#нахождение n-ого простого числа
import cProfile
def simple_2(n):
    lst=[2]

    for i in range(3, int(n), 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst

'''Время выполнения через timeit'''
#python -m timeit -n 100 -s "import simple_2" "simple_2.simple_2(1111)"100 loops, best of 3: 290 usec per loop
#python -m timeit -n 100 -s "import simple_2" "simple_2.simple_2(111)"100 loops, best of 3: 18.3 usec per loop
#python -m timeit -n 100 -s "import simple_2" "simple_2.simple_2(11)"100 loops, best of 3: 1.38 usec per loop

#cProfile.run('simple_2(10000)')
'''
         1232 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.005    0.005    0.005    0.005 simple_2.py:3(simple_2)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
     1228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


#cProfile.run('simple_2(1000)')

'''
         171 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 simple_2.py:3(simple_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      167    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
