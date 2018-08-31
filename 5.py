_author_= 'Швец Александр Николаевич'
#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-10,10) for _ in range (10)]
print(f'наш массив: {a}')

max_el = 0
max_ind = 0

for x in a:
    if x < max_el:
        max_el = x

if max_el >= 0:
    print('Не повезло с рандомизацией массива, нет отрицательных чисел')
else:
    for x in range(len(a)):
        if a[x] < 0 and a[x] > max_el:
            max_el = a[x]
            max_ind = x
    print(f'максимальный отрицательный элемент: {max_el}, его индекс: {max_ind} ')