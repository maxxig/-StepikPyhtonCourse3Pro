from random import choice
def random_numbers(left, right):
    def func():
        return choice(list(range(left, right+1)))
    return iter(func, 'stop')


iterator = random_numbers(-100, 99)

print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))