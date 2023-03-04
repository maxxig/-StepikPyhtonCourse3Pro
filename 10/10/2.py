from itertools import pairwise
def is_rising(iterable):
    return (all(map(lambda x: True if x[0] < x[1] else False, pairwise(iterable))))

# TEST_4:
iterator = iter(list(range(200, 100, -1)))

print(is_rising(iterator))

# TEST_5:
iterator = iter(list(range(100, 201)) + [200])

print(is_rising(iterator))

# TEST_6:
iterator = iter([10]*50)

print(is_rising(iterator))