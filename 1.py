_author_= 'Швец Александр Николаевич'
# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random

a = [random.randint(-100, 100) for _ in range(40)]

print(f'исходный массив - \n {a}')

CHANGES = True
z = 1

while CHANGES:
    CHANGES = False
    for x in range(len(a) - z):
        if a[x] > a[x+1]:
            a[x], a[x+1] = a[x+1], a[x]
            CHANGES = True
    z += 1

print(f'итоговый массив - \n {a}')
