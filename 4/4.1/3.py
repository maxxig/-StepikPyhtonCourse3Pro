import sys
cnt, last_number = 0, None
for l in sys.stdin:
    last_number = int(l)
    cnt += 1

if last_number % 2 == 0:
    if cnt % 2 == 1:
        print('Анри')
    else:
        print('Дима')
elif last_number % 2 == 1:
    if cnt % 2 == 1:
        print('Дима')
    else:
        print('Анри')