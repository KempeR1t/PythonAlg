_author_= 'Швец Александр Николаевич'
from collections import namedtuple

Firma = namedtuple('Firma', 'name kv1 kv2 kv3 kv4 sr_za_god')

a = int(input('Сколько вы хотите ввести предприятий? : '))

itog = []

for x in range(a):
    name = input('Введите имя предприятия: ')
    kv1 = int(input('Введите выручку за 1 квартал: '))
    kv2 = int(input('Введите выручку за 2 квартал: '))
    kv3 = int(input('Введите выручку за 3 квартал: '))
    kv4 = int(input('Введите выручку за 4 квартал: '))
    sr = (kv1 + kv2 + kv3 + kv4) / 4
    nasha_firma = Firma(name, kv1, kv2, kv3, kv4, sr)
    itog.append(nasha_firma)

summa_deneg = 0

for x in range(a):
    summa_deneg += (itog[x].kv1 + itog[x].kv2 + itog[x].kv3 + itog[x].kv4)

print(f'Столько всего заработали все фирмы вместе взятые - {summa_deneg}')

obshee_srednee = summa_deneg / (4 * a)
print(f'это средняя годовая выручка среди всех фирм - {obshee_srednee}')

menshe = []
bolshe = []

for x in range(a):
    if itog[x].sr_za_god < obshee_srednee:
        menshe.append(itog[x].name)
    else:
        bolshe.append(itog[x].name)

print(f'Список фирм с выручкой меньше среднего - {menshe}, а у этих больше - {bolshe}')
