_author_= 'Швец Александр Николаевич'
#Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ»
print('Таблица ASCII элементов 32 по 127 включительно')
for x in range(32,128):
    if (x - 32) % 10 == 0 and x != 32:
        print()
    print(x,'-',chr(x), end = '   ')