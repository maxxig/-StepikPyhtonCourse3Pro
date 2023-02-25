from itertools import  dropwhile
def drop_this(iterable, obj):
    return dropwhile(lambda x: x == obj, iterable)

# TEST_4:
letters = drop_this(iter('stepik'), 'g')

print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))

# TEST_5:
numbers = drop_this(map(abs, range(100)), -1)

print(*numbers)

# TEST_6:
iterator = iter([5, 5, 5, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])

print(*drop_this(iterator, 5))

# TEST_7:
print(list(drop_this('b', 'b')))

# TEST_8:
print(list(drop_this('a', 'b')))

# TEST_9:
print(list(drop_this([], None)))