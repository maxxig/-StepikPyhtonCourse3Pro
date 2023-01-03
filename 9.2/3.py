import sys
lines = [i for i in sys.stdin]
max_value = eval(lines[0])
for l in lines:
    v = eval((l))
    if v > max_value:
        max_value = v
print(max_value)