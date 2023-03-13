from itertools import combinations_with_replacement, groupby
wallet = [100, 50, 20, 10, 5]


d, count = [], 0
for i in range(1, int(100/min(wallet))+1):
    s = combinations_with_replacement(wallet, i)
    res = groupby(map(lambda x: sorted(x), filter(lambda x: sum(x) == 100, s)))
    for k, r in res:
        d.append(k)
        count += 1

print(len(d))