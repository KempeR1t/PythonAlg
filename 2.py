_author_= 'Швец Александр Николаевич'
#Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено
# число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)
a  = int(input('Введите натуральное число '))
chet=0
nechet=0
for i in str(a):
    if int(i) % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(f'В нашем числе {a} было {chet} четных цифр и {nechet} нечетных цифр')