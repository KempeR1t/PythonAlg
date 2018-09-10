_author_= 'Швец Александр Николаевич'
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

#вариант маньяческий, когда мы работаем посимвольно только 16-чной системой исчисления и ничего более
'''
Принцип работы программы: Задаем 2 словаря для соотношений 16чных чисел с 10чными, в одном ключи это 10 чные, а во втором
наоборот. После этого нужно понять какое из введенных чисел длиннее, затем начинаем их складывать. Сложение происходит
"столбиком" ставим 2 числа друг под другом и посимвольно складываем их, результат сложения округленный записываем, а
оставшееся ( при наличии) переносим в следуюший разряд. Умножение это такое же сложение, просто много раз. Более подробные
комментарии внутри кода.
'''
from collections import deque

sixteen =  {str(a): a for a in range(16)}
sixteen2 = {a: str(a) for a in range(16)}

for x in range(10,16):
    sixteen[chr(x+87)] = sixteen.pop(str(x))
    sixteen2[x] = chr(x + 87)                             #генерируем словари для работы

print(sixteen)
print(sixteen2)

a = deque(input('Введите первое шестнадцатеричное число ').lower())
b = deque(input('Введите второе шестнадцатеричное число ').lower())

if len(a) > len(b):                                     # смотрит какое из чисел длиннее
    marker = True
else:
    marker = False

def summa(a,b):                                         #функция суммирует 2 числа в 16чном виде
    if len(a) > len(b):                                 #смотрим какое из поданных чисел длиннее
        length = len(b)
    else:
        length = len(a)
    x=-1
    extra = '0'
    new = deque()
    while abs(x) < length+1:                           #дальше мы начинаем посимвольно складывать числа начиная с последнего
        if (sixteen[a[x]] + sixteen[b[x]] + sixteen[extra]) > 15:    #если сумма больше 15, то берем остаток
            new.appendleft(sixteen2[(sixteen[a[x]] + sixteen[b[x]] + sixteen[extra])% 16]) #а все остальное помещаем
            extra = str((sixteen[a[x]] + sixteen[b[x]] + sixteen[extra]) // 16) #в переменную , и переносим на след разряд
            if int(extra) > 9:
                extra = sixteen2[int(extra)]      #доп проверки
        else:
            new.appendleft(sixteen2[sixteen[a[x]] + sixteen[b[x]] + sixteen[extra]] )
            extra = '0'                                     #в итоге мы получаем сумму этих двух чисел без самого
        x -= 1                                              #высокого разряда, мы  в след функции будем смотреть что с ним
    return new,extra                                        #делать

def proizv(a , b):                                          #функция работает точно так же как сложение, только умножает
    x = -1                                                  #посимвольно
    if len(a) > len(b):                                     #я беру большее число и по очереди умножаю его на каждый символ
        length = len(a)                                     #меньшего
        max = sixteen[a[x]]
        min = sixteen[b[-1]]
    else:
        length = len(b)
        min = sixteen[a[-1]]
        max = sixteen[b[x]]
    extra = '0'
    new = deque()
    while abs(x) < length + 1:
        mix = max * min + sixteen[extra]
        if mix > 15:
            new.appendleft(sixteen2[(mix) % 16])
            extra = str((mix) // 16)
            if int(extra) > 9:
                extra = sixteen2[int(extra)]
        else:
            new.appendleft(sixteen2[mix])
            extra = '0'
        x -= 1
    new.appendleft(sixteen2[sixteen[extra]])
    return new

def ostatok(new, extra, a, b):                       #функция суммирования чисел суммировала лишь то количество разрядов
    if len(a) == len(b):                             # которое было в коротком числе, а затем мне нужно было в сумму
        if extra != '0':                             #снести остальные разряды длинного числа
            new.appendleft(str(sixteen[extra]))      #если у меня остаток 0 , то просто сносим остальные разряды длинного
    elif len(a) > len(b):                            #числа в сумму, в противном случае к оставшейся части прибавляем остаток
        if extra !='0':
            _extra = deque(extra)
            while len(_extra) < (len(a)-len(b)):
                _extra.appendleft('0')
            _a = deque(list(a)[:len(a)-len(b)])
            new.appendleft(summa(_a,_extra)[0])
            if summa(_a,_extra)[1] != '0':
                new.appendleft(summa(_a, _extra)[1])
        else:
            new.appendleft(list(a)[:len(a)-len(b)])
    elif len(a) < len(b):
        if extra !='0':
            _extra = deque(extra)
            while len(_extra) < (len(b)-len(a)):
                _extra.appendleft('0')
            _b = deque(list(b)[:len(b)-len(a)])
            new.appendleft(summa(_b,_extra)[0])
            if summa(_b,_extra)[1] != '0':
                new.appendleft(summa(_b, _extra)[1])
        else:
            new.appendleft(list(b)[:len(b) - len(a)])
    return new
new_summa = ostatok(summa(a,b)[0], summa(a,b)[1],a,b)

full_proizv = deque('0')
full_proizv2 = deque()

for x in range(len(b) if marker else len(a)):        #а вот тут мы умножаем.
    proizvedenie = proizv(a,b)                #определяем какое из чисел короче и дальше мы будем более длинное поочередно
    for z in range(x):                        #умножать на каждый символ короткого
        proizvedenie.append('0')              #умножили на 1 символ, затем по правилу умножения в столбик увеличваем разрядность
    if marker:                                #затем из переменной короткой убираем последний разряд чтобы умножать уже
        b.pop()                               #уже на следующий
    else:
        a.pop()
    full_proizv = ostatok(summa(full_proizv,proizvedenie)[0], summa(full_proizv,proizvedenie)[1],full_proizv,proizvedenie)
    for x in range(len(full_proizv)):
        for j in range(len(full_proizv[x])):  #вот этот маленький цикл нужен был чтобы привести результат к тому виду,
            full_proizv2.append(full_proizv[x][j]) #который способа принимать моя функция
    full_proizv = full_proizv2
    full_proizv2 = deque()


def vivod(nice):                           #делаем красивый вывод
    itog = ''
    for x in range(len(nice)):
        for j in range(len(nice[x])):
            itog += nice[x][j]
    return itog

itog_summa = vivod(new_summa)
itog_proizv = vivod(full_proizv)


print(f'сумма будет  равна - {itog_summa.upper()}, а произведение - {itog_proizv.upper()}')