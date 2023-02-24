from itertools import count, cycle
def alnum_sequence():
     return cycle(' '.join([f"{i[0]} {chr(i[1])}" for i in zip(count(1), range(65, 91))]).split())


# TEST_3:
alnum = alnum_sequence()

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))

# TEST_4:
alnum = alnum_sequence()

for _ in range(10_000):
    next(alnum)

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))

# TEST_5:
alnum = alnum_sequence()

for _ in range(100_000):
    next(alnum)

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))