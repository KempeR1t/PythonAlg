_author_= 'Швец Александр Николаевич'

import sys

def show_size(x, level = 0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, '__item__'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)

#****************************************************************************************************************

#Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
a = int(input('Сколько чисел хотите ввести? '))

max_chislo = 0
max_summa = 0

def summa_cifr(chislo):
    summa = 0
    for x in str(chislo):
        summa += int(x)
    return summa

for x in range(a):
    b = int(input('Введите число '))
    if summa_cifr(b) > max_summa:
        max_summa = summa_cifr(b)
        max_chislo = b
    else:
        pass
print(f'Наибольшей суммой цифр - {max_summa} обладает число - {max_chislo}')

show_size(a)
#  type = <class 'int'>, size = 28, object = 5
show_size(max_summa)
#  type = <class 'int'>, size = 28, object = 5
show_size(max_chislo)
#  type = <class 'int'>, size = 28, object = 5

#******************************************************************************************************************

#Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.


print('Для заполнения матрицы введите числа')
a = [[int(input(f'строка: {z+1}, столбец: {x+1} '))
      for z in range (4)] for x in range(4)]

for row in a:
    summa = 0
    for x in range(len(row)):
        summa += row[x]
    row.append(summa)

print()
print('Так выглядит наш массив:')
for row in a:
    print(row)

show_size(row)
 # type = <class 'list'>, size = 128, object = [13, 14, 15, 16, 58]
	#  type = <class 'int'>, size = 28, object = 13
	#  type = <class 'int'>, size = 28, object = 14
	#  type = <class 'int'>, size = 28, object = 15
	#  type = <class 'int'>, size = 28, object = 16
	#  type = <class 'int'>, size = 28, object = 58
show_size(a)
# type = <class 'list'>, size = 96, object = [[1, 2, 3, 4, 10], [5, 6, 7, 8, 26], [9, 10, 11, 12, 42], [13, 14, 15, 16, 58]]
# 	 type = <class 'list'>, size = 128, object = [1, 2, 3, 4, 10]
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 2
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 4
# 		 type = <class 'int'>, size = 28, object = 10
# 	 type = <class 'list'>, size = 128, object = [5, 6, 7, 8, 26]
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 6
# 		 type = <class 'int'>, size = 28, object = 7
# 		 type = <class 'int'>, size = 28, object = 8
# 		 type = <class 'int'>, size = 28, object = 26
# 	 type = <class 'list'>, size = 128, object = [9, 10, 11, 12, 42]
# 		 type = <class 'int'>, size = 28, object = 9
# 		 type = <class 'int'>, size = 28, object = 10
# 		 type = <class 'int'>, size = 28, object = 11
# 		 type = <class 'int'>, size = 28, object = 12
# 		 type = <class 'int'>, size = 28, object = 42
# 	 type = <class 'list'>, size = 128, object = [13, 14, 15, 16, 58]
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 28, object = 14
# 		 type = <class 'int'>, size = 28, object = 15
# 		 type = <class 'int'>, size = 28, object = 16
# 		 type = <class 'int'>, size = 28, object = 58
show_size(summa)
#  type = <class 'int'>, size = 28, object = 58

#****************************************************************************************************************

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

show_size(a)
# type = <class 'list'>, size = 128, object = [[47, 26, 38, 84, 88], [29, 66, 16, 59, 21], [21, 29, 50, 21, 0], [97, 72, 83, 60, 16], [15, 18, 11, 47, 86]]
# 	 type = <class 'list'>, size = 128, object = [47, 26, 38, 84, 88]
# 		 type = <class 'int'>, size = 28, object = 47
# 		 type = <class 'int'>, size = 28, object = 26
# 		 type = <class 'int'>, size = 28, object = 38
# 		 type = <class 'int'>, size = 28, object = 84
# 		 type = <class 'int'>, size = 28, object = 88
# 	 type = <class 'list'>, size = 128, object = [29, 66, 16, 59, 21]
# 		 type = <class 'int'>, size = 28, object = 29
# 		 type = <class 'int'>, size = 28, object = 66
# 		 type = <class 'int'>, size = 28, object = 16
# 		 type = <class 'int'>, size = 28, object = 59
# 		 type = <class 'int'>, size = 28, object = 21
# 	 type = <class 'list'>, size = 128, object = [21, 29, 50, 21, 0]
# 		 type = <class 'int'>, size = 28, object = 21
# 		 type = <class 'int'>, size = 28, object = 29
# 		 type = <class 'int'>, size = 28, object = 50
# 		 type = <class 'int'>, size = 28, object = 21
# 		 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'list'>, size = 128, object = [97, 72, 83, 60, 16]
# 		 type = <class 'int'>, size = 28, object = 97
# 		 type = <class 'int'>, size = 28, object = 72
# 		 type = <class 'int'>, size = 28, object = 83
# 		 type = <class 'int'>, size = 28, object = 60
# 		 type = <class 'int'>, size = 28, object = 16
# 	 type = <class 'list'>, size = 128, object = [15, 18, 11, 47, 86]
# 		 type = <class 'int'>, size = 28, object = 15
# 		 type = <class 'int'>, size = 28, object = 18
# 		 type = <class 'int'>, size = 28, object = 11
# 		 type = <class 'int'>, size = 28, object = 47
# 		 type = <class 'int'>, size = 28, object = 86
show_size(c)
# type = <class 'list'>, size = 128, object = [15, 18, 11, 21, 0]
# 	 type = <class 'int'>, size = 28, object = 15
# 	 type = <class 'int'>, size = 28, object = 18
# 	 type = <class 'int'>, size = 28, object = 11
# 	 type = <class 'int'>, size = 28, object = 21
# 	 type = <class 'int'>, size = 24, object = 0
show_size(min_el)
# type = <class 'int'>, size = 28, object = 21

