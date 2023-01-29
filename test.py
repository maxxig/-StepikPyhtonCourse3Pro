numbers = (-2, -1, 0, 1, 2)

non_zero = filter(None, numbers)
positive = map(abs, non_zero)

print(*positive)