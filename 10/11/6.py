from itertools import groupby
def ranges(numbers):
    _number = [(v-k, v) for k, v in enumerate(numbers)]
    res = groupby(_number, key=lambda x: x[0])
    res2 = [[i[1] for i in item] for k, item in res]
    return [(min(r), max(r)) for r in res2]

# TEST_4:
numbers = list(range(5, 101))

print(ranges(numbers))

# TEST_5:
numbers = list(range(10, 21)) + [30] + list(range(35, 101)) + list(range(1000, 1001))

print(ranges(numbers))