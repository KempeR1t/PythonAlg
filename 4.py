_author_= 'Швец Александр Николаевич'
#Определить, какое число в массиве встречается чаще всего.
import random

a = [random.randint(0,10) for _ in range (20)]
print(f'наш массив - {a}')

max_chislo = a[0]
max_povtori = 0

for x in a:
    povtori = 0
    for z in a:
        if x == z:
            povtori += 1
    if povtori > max_povtori:
        max_povtori = povtori
        max_chislo = x

print(f'больше всего раз - {max_povtori} встретилось число {max_chislo}')