from itertools import combinations, groupby
wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

d, count = [], 0
for i in range(1, len(wallet)+1):
    s = combinations(wallet, i)
    #res = map(lambda x: sorted(x),filter(lambda x: sum(x) == 100, s))
    res = groupby(map(lambda x: sorted(x),filter(lambda x: sum(x) == 100, s)))
    for k, r in res:
        d.append(k)
        count += 1

my_set = set()
for s in d:
    my_set.add(tuple(s))
print(len(my_set))
