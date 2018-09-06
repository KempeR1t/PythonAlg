# без решета
def simple_2(n):
    lst = [2]
    i = 3
    while len(lst) < int(n):
        for j in lst:
            if i % j == 0:
                i += 2
                break
        else:
            lst.append(i)
            i+=2
    return lst[-1]

print(simple_2(11))
