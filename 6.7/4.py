from collections import Counter
from functools import reduce


cn = Counter(input().split(','))

def sum(a,b):
    return a+b

def get_price(word):
    return reduce(sum, list(
        list(filter(lambda x:x >=1072 and x <= 1104, map(lambda x:ord(x) , word)))
    ), 0)

max_len = len(max(cn.keys(), key=lambda x: len(x)))

for k, v in sorted(cn.items(), key= lambda x:x[0]):
    price = get_price(k)
    print(f"{k.ljust(max_len,' ')}: {price} UC x {v} = {price * v} UC")