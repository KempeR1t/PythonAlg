_author_= 'Швец Александр Николаевич'
#Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

a = [[random.randint(0,100) for _ in range (5)] for x in range(5)]

c=[]

print('Так выглядит наш массив:')
for row in a:
    print(row)

print()

for x in range(5):
    print(f'Наш {x+1} стобец выглядит так')
    min_el = [row[x] for row in a][0]
    print([row[x] for row in a])
    for z in range(len([row[x] for row in a])):
        if [row[x] for row in a][z] < min_el:
            min_el = [row[x] for row in a][z]
    print(f'Его минимальный элемент это - {min_el}')
    c.append(min_el)
    print()

for x in c:
    if x > min_el:
        min_el = x

print(f'а самым большим из минимальных элементов становится - {min_el}')