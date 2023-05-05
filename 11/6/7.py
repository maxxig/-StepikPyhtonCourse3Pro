import re, sys
cnt = 0
for line in sys.stdin:
    if re.search(r'(BEEGEEK)', line, flags=re.IGNORECASE):
        cnt +=1
print(cnt)
