import sys
cnt = 0
for line in sys.stdin:
    if line.lstrip()[0] == '#':
        cnt += 1

print(cnt)