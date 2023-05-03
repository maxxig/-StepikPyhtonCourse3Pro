from re import search
import sys
goals = 0
for line in sys.stdin:
    if search(r'^(beegeek).*(beegeek)$', line):
        goals += 3
    elif search(r'(^(beegeek).*)|(.*(beegeek)$)', line):
        goals += 2
    elif search(r'^.{1,}(beegeek).{1,}$', line):
        goals += 1
print(goals)