_author_= 'Швец Александр Николаевич'
#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = [random.randint(0,100) for _ in range (10)]

print(f'наш массив: {a}')

max_el, min_el = a[0], a[0]
max_ind , min_ind = 0, 0

for x in range(len(a)):
    if a[x] > max_el:
        max_el = a[x]
        max_ind = x

for x in range(len(a)):
    if a[x] < min_el:
        min_el = a[x]
        min_ind = x

print(f'Максимальный эл-т: {max_el} имеет индекс: {max_ind}, минимальный эл-т: {min_el} имеет индекс: {min_ind}')

summa = 0

if max_ind > min_ind:
    for x in range(min_ind+1,max_ind):
        summa += a[x]
    print(f'сумма элементов с индексами с {min_ind+1} по {max_ind-1} будет {summa}')
else:
    for x in range(max_ind+1,min_ind):
        summa += a[x]
    print(f'сумма элементов с индексами с {max_ind+1} по {min_ind-1} будет {summa}')
