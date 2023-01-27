def filterfalse(predicate, iterable):
    return  filter(lambda x: not bool(x), iterable) if predicate is None else filter(lambda x: not predicate(x), iterable)



# objects = [0, 1, True, False, 17, []]
# print(*filterfalse(None, objects))

# numbers = (1, 2, 3, 4, 5)
# print(*filterfalse(lambda x: x % 2 == 0, numbers))

# numbers = [1, 2, 3, 4, 5]
#
# print(*filterfalse(lambda x: x >= 3, numbers))

objects = [0, 0, 0, True, False, 1788, [], {}, set(), (), '', 0.0, None, 'stepik', dict()]

print(*filterfalse(None, objects))