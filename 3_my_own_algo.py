# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.


'''
Первый вариант решения.
'''

import random

array = [random.randint(-100, 100) for _ in range(41)]
array2 = array[:]
array2.sort()

if len(array) % 2 != 1:
    print('Не пытайся меня обмануть, в этом массиве не будет медианы')

else:
    print(f'исходный массив - \n {array}')
    print('*' * 200)
    print(f'исходный массив в сортированном виде для наглядности - \n {array2}')
    print('*' * 200)

    for CHISLO1 in array:
        bolshe = []
        menshe = []
        ravno = []
        for CHISLO2 in array:
            if CHISLO2 < CHISLO1 :
                menshe.append(CHISLO2)
            elif CHISLO2 > CHISLO1:
                bolshe.append(CHISLO2)
            else:
                ravno.append(CHISLO2)
        if abs(len(menshe) - len(bolshe)) == len(ravno) - 1:
            print(f'Медианой является  число: {ravno[0]}')
            exit()
