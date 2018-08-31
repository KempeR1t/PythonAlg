_author_= 'Швец Александр Николаевич'
#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(10,99) for _ in range (10)]
print(f'наш массив до перестановки:    {a}')
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

a[max_ind], a[min_ind] = a[min_ind], a[max_ind]
print(f'наш массив после перестановки: {a}')