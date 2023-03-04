from itertools import pairwise

def max_pair(iterable):
    return max(map(lambda x: x[0] + x[1], pairwise(iterable)))

# TEST_4:
iterator = iter([10, 11])

print(max_pair(iterator))

# TEST_5:
iterator = iter([5, 6, 4, 3, 2, 2])

print(max_pair(iterator))

# TEST_6:
iterator = iter([10, 10, 10, 10, 10, 10, 10, 10, 10])

print(max_pair(iterator))

# TEST_7:
iterator = iter([11, 10, 19, 1, 12, 100, 1, 13, 1])

print(max_pair(iterator))

# TEST_8:
iterator = iter([11, 10, 19, 1, 12, 100, 1, 13, 107])

print(max_pair(iterator))