def alternating_sequence(count = None):
    res = 1
    while(1):
        yield res
        res += 1
        if count != None and res > count:
            return
        yield -res
        res += 1
        if count != None and res > count:
            return



generator = alternating_sequence(50)

for _ in generator:
    pass

try:
    next(generator)
except StopIteration:
    print('Error')