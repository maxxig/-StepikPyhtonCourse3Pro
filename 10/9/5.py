from itertools import islice

def take_nth(iterable, n):
    res = None
    try:
        res = next(islice(iterable, n-1, n))
        #print(*islice(iterable, n-1, n))
    except:
        res = None
    return res

# TEST_4:
iterator = iter('beegeek')

print(take_nth(iterator, 1))

# TEST_5:
iterator = tuple('stepik')

print(take_nth(iterator, 6))

# TEST_6:
iterator = iter('p')

print(take_nth(iterator, 1))

# TEST_7:
iterator = iter('p')

print(take_nth(iterator, 2))

# TEST_8:
iterator = iter('beegeek')

print(take_nth(iterator, 7))

# TEST_9:
iterator = iter('beegeek')

print(take_nth(iterator, 8))

# TEST_10:
print(take_nth([], 4))