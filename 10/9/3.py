from itertools import dropwhile
def first_true(iterable, predicate):
    res = None
    if predicate is None:
        predicate = bool
    try:
        res = next(dropwhile(lambda x: not predicate(x), iterable))
    except:
        res = None
    return res


# TEST_4:
numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)

print(first_true(numbers_iter, lambda num: num < 0))

# TEST_5:
numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 0))

# TEST_6:
numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 1))

# TEST_7:
numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num == 200))

# TEST_8:
numbers = iter([])

print(first_true(numbers, lambda num: num == 200))