import sys
for line in sys.stdin:
    print(line[::-1].strip(), sep='')