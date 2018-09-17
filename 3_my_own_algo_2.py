# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.


'''
Второй вариант решения
'''

import random

def minimum(array_):
    min = array[0]
    for x in array:
        if x < min:
            min = x
    return min

array = [random.randint(-100, 100) for _ in range(41)]
array2 = array[:]
array2.sort()

length = len(array)

print(f'исходный массив - \n {array}')
print('*' * 200)
print(f'исходный массив в сортированном виде для наглядности - \n {array2}')
print('*' * 200)


while len(array) > (length -  1) / 2 + 1:
    array.remove(minimum(array))

print(f'Медианой является  число: {minimum(array)}')
