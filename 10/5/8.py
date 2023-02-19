def palindromes():
    i = 0
    while(1):
        i += 1
        if str(i) == str(i)[::-1]:
            yield i


generator = palindromes()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))