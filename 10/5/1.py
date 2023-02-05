def simple_sequence():
    res = 0
    while(1):
        res += 1
        for i in range(res):
            yield res



generator = simple_sequence()

for _ in range(10_000_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))