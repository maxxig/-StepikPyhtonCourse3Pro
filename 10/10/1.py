from itertools import chain
def sum_of_digits(iterable):
    res = 0
    for i in chain(iterable):
        for _i in chain(str(i)):
            res += int(_i)
    return res

# TEST_4:
numbers = [10]*100

iterator = iter(numbers)
print(sum_of_digits(iterator))

# TEST_5:
numbers = [100, 20, 30, 400, 500, 5]*100000

print(sum_of_digits(numbers))