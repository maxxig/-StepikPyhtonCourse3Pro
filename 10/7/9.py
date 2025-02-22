def stop_on(iterable, obj):
    for i in iterable:
        if i == obj:
            return
        else:
            yield i

# INPUT DATA:

# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))

# TEST_2:
iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))

# TEST_3:
data = map(abs, range(-100, 100))

iterator = stop_on(data, 76)

print(*iterator)

# TEST_4:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

iterator = stop_on(data, 'o')

print(*iterator)

# TEST_5:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

iterator = stop_on(data, 'e')

print(*iterator)

# TEST_6:
data = 'g'

iterator = stop_on(data, 'g')

print(*iterator)

# TEST_7:
data = 'eeeeeeeeeeeeee'

iterator = stop_on(data, 'e')

print(*iterator)

# TEST_8:
data = iter('qweretqwewerqweqwerewr')

iterator = stop_on(data, 'H')

print(*iterator)

# TEST_9:
data = iter('beegeek')

iterator = stop_on(data, 'g')

print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print('Error')

# TEST_10:
data = ['bee', 'geek', 'stepik', 'python']

print(*stop_on(data, 'stepik'))

# TEST_11:
data = []

print(list(stop_on(data, 'stepik')))
