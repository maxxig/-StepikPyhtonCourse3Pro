from itertools import accumulate
import operator
def factorials(n):
    return accumulate(range(1, n+1), operator.mul)

# TEST_3:
numbers = factorials(100)

print(*numbers)

# TEST_4:
numbers = factorials(1001)

for _ in range(1000):
    next(numbers)

print(next(numbers))