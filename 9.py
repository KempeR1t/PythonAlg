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