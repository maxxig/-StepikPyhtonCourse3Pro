def hash_as_key(objects):
    res = {}
    for o in objects:
        if hash(o) not in res:
            res[hash(o)] = o
        else:
            if isinstance(res[hash(o)], list):
                res[hash(o)].append(o)
            else:
                t = [res[hash(o)]]
                t.append(o)
                res[hash(o)] = t
    return res

data = [(1, 2, 3, (100, 200, 300)), (frozenset((90, 100, 110)), 10, 222), ((100, 200, 3300), (100, 100)), 900, 999, 1000, 999999999991, (123123123, 234234234, 2342354536758578), 900, 1000000, 1000]

print(hash_as_key(data))