# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
#n1 = int(input("Введите первое двоичное число: "))
#n2 = int(input("Введите второе двоичное число: "))
n1 = 5
n2 = 6
print('Наши числа = ', n1, n2)
print('Результат побитового ИЛИ =',n1 | n2, 'Результат побитового ИЛИ в двоичном виде =', bin(n1 | n2))
print('Результат побитового И =', n1 & n2, 'Результат побитового И в двоичном виде=', bin(n1 & n2))
print('Побитовый сдвиг справа на 2 числа 5 =', 5>>2, 'Побитовый сдвиг слева на 2 числа 5 =', 5<<2)
print('Объяснение:')
print('2 числа представляются в 10-чном формате и побитно складываются либо умножаются')
print('при двоичных сдвигах мы сдвигаем все биты числа в указанном направлении на указанное число разделов,  ')
print('пустые элементы заполняются нулями если число положительное, либо единицами если оно отрицательное')