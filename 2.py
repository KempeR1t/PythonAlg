_author_= 'Швец Александр Николаевич'
# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.
from heapq import heappush, heappop, heapify
import collections

def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


# txt = input('Введите строку для кодирования: ')
txt = 'beep bop beer!'

symb2freq = collections.defaultdict(int)

for ch in txt:
    symb2freq[ch] += 1

symb2freq = collections.Counter(txt)
huff = encode(symb2freq)

print('Таблица кодирования')
for p in huff:
    print("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))

print('*' * 50)
print(f'Наша строка в исходном виде \n{txt}')

print('*' * 50)
print('Наша строка в закодированном виде')
for z in txt:
    for v in huff:
        if z in v:
            print(v[1], end= ' ')
print('\n'+'*' * 50)