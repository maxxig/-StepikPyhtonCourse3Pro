def primes(left, right):
    for i in range(left, right+1):
        is_find = False
        for j in range(2, i):
            if i % j == 0 and i != j:
                is_find = True
                break
        if not is_find and i != 1:
            yield i
    return

generator = primes(43, 72)

print(*generator)