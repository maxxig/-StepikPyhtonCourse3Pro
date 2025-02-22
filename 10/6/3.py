def count_iterable(iterable):
    return (sum(map(lambda x: 1, iterable)))
    #return sum((1 for i in iterable))

# INPUT DATA:

# TEST_1:
print(count_iterable([1, 2, 3, 4, 5]))

# TEST_2:
numbers = iter([1, 2, 3, 4, 5, 6, 7])

print(count_iterable(numbers))

# TEST_3:
data = tuple(range(432, 3845, 17))

print(count_iterable(data))

# TEST_4:
data = map(abs, range(-200, 400, 11))

print(count_iterable(data))

# TEST_5:
data = filter(lambda x: x % 13, range(101, 982))

print(count_iterable(data))

# TEST_6:
data = zip('beegeek', 'stepik')

print(count_iterable(data))

# TEST_7:
data = zip('', '')

print(count_iterable(data))

# TEST_8:
data = filter(None, range(100_000_001))

print(count_iterable(data))
