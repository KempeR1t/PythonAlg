_author_= 'Швец Александр Николаевич'
#В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

def minimum(b):
    min_el = b[0]
    min_ind = 0
    for x in range(len(b)):
        if b[x] < min_el:
            min_el = b[x]
            min_ind = x
    return min_el, min_ind

a = [random.randint(0,100) for _ in range (10)]

print(f'наш массив: {a}')
print(f'Самое маленькое число в массиве: {minimum(a)[0]}')

a.pop(minimum(a)[1])

print(f'Вторым с конца будет число: {minimum(a)[0]}')