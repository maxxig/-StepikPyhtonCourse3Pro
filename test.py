from itertools import repeat

for a, b, c in map(lambda x, у: (x, у, x * у), repeat(2), range(6)):
    print(f'{a} * {b} = {c}')