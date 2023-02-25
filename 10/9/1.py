from itertools import dropwhile
def drop_while_negative(iterable):
    return dropwhile(lambda x: x < 0, iterable)

# TEST_4:
iterator = iter([0, 1, 2, 3, 4, 5, 6, 7])

print(list(drop_while_negative(iterator)))

# TEST_5:
iterator = iter([-1, -2, -3, -4, -5, -6, 7])

print(*drop_while_negative(iterator))

# TEST_6:
iterator = iter([-1, 2, 3, 4, 5, 6, 7, 8])

print(*drop_while_negative(iterator))

# TEST_7:
iterator = iter([1])

print(*drop_while_negative(iterator))

# TEST_8:
iterator = iter([-1])

print(list(drop_while_negative(iterator)))

# TEST_9:
iterator = iter([])

print(list(drop_while_negative(iterator)))