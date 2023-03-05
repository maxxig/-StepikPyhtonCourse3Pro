from itertools import groupby
str = input().split()
str = sorted(str, key=lambda x: (len(x),x))

_t = [(key, list(item)) for key,item in groupby(str, key = lambda x: len(x))]

for k, item in sorted(_t, key=lambda x:x[0]):
    print(k, '->', ', '.join(sorted(item)))
