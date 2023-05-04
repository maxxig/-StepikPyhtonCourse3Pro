from re import search
import sys
cnt_bee, cnt_geek = 0, 0

for line in sys.stdin:
    if search(r'bee.*bee', line):
        cnt_bee += 1
    if search(r'\bgeek\b', line):
        cnt_geek += 1

print(cnt_bee)
print(cnt_geek  )