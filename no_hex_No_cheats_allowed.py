_author_= 'Швец Александр Николаевич'
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

#Вариант 1 - полухитрый, т.к. работаем с 10-системой исчисления. Написан  за 10 минут
from collections import deque

sixteen =  {str(a): a for a in range(16)}
sixteen2 = {a: str(a) for a in range(16)}

for x in range(10,16):
    sixteen[chr(x+87)] = sixteen.pop(str(x))
    sixteen2[x] = chr(x + 87)

a = deque(input('Введите первое шестнадцатеричное число '))
b = deque(input('Введите второе шестнадцатеричное число '))

def sixtoten(q):
    x = -1
    z = 0
    while abs(x) < len(q) + 1:
        z += sixteen[q[x]] * (16 ** (abs(x) - 1))
        x -= 1
    return z

def tentosix(qq):
    six = deque()
    while qq != 0:
        six.appendleft(sixteen2[qq % 16])
        qq = qq // 16
    six2 = six
    six = ''
    for x in six2:
        six += x
    return six.upper()

print(f'Суммой {a} и {b} будет - {tentosix(sixtoten(a)+sixtoten(b))} , а их произведением - '
      f'{tentosix(sixtoten(a)*sixtoten(b))}')
