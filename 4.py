#Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
print('Последовательно вида 1 -0.5 0.25 -0.125 ...')
def posledovatelnost(a, summa=1):
    if a == 1:
        return summa
    else:
        return summa + posledovatelnost(a - 1, summa / (-2))
vvod = int(input('Введите количество элементов, которые вы хотите просуммировать , но не более 900 '))
print(f'сумма = {posledovatelnost(vvod)}')