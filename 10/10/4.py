from itertools import chain, tee
def ncycles(iterable, times):
    return chain.from_iterable(tee(iterable, times))

# TEST_4:
iterator = ncycles(iter('b'), 1)

print(next(iterator))

# TEST_5:
iterator = ncycles(iter('g'), 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_6:
iterator = ncycles(iter([10, 10, 10, 10, 10]), 5)

print(*iterator)

# TEST_7:
print(list(ncycles([], 5)))