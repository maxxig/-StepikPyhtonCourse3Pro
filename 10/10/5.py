from itertools import zip_longest
def grouper(iterable, n):
    _it = iter(iterable)
    return zip_longest(*(_it for i in range(n)), fillvalue=None)

# TEST_4:
iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 4))

# TEST_5:
iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 5))

# TEST_6:
iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 1))

# TEST_7:
iterator = iter('beegeek')

print(*grouper(iterator, 5))

# TEST_8:
iterator = iter('beegeek')

print(*grouper(iterator, 20))