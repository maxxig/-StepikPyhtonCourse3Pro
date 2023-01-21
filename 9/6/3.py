def cyclic_shift(numbers: list[int | float], step: int) -> None:
    ln = len(numbers)
    if step > 0:
        for i in range(abs(step)):
            n = numbers.pop()
            numbers.insert(0,  n)
    elif step < 0:
        for i in range(abs(step)):
            n = numbers.pop(0)
            numbers.insert(ln-1, n)

numbers = [234, 235]
cyclic_shift(numbers, -22)

print(cyclic_shift(numbers, -22))