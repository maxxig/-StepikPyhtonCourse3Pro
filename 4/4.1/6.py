import sys

for line in sys.stdin:
    if len(line.lstrip()) > 0 and line.lstrip()[0] == '#':
        continue
    else:
        sys.stdout.write(line)