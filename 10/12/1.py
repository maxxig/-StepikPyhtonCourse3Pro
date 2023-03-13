from itertools import permutations
test = input()
s = set()
for p in permutations(test, len(test)):
    s.add(''.join(p))
_s = sorted([i for i in s])
print(*_s, sep='\n')