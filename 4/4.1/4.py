import sys
ar = [int(line.rstrip()) for line in sys.stdin]

if len(ar) < 1:
    print('нет учеников')
else:
    print(f'Рост самого низкого ученика: {min(ar)}')
    print(f'Рост самого высокого ученика: {max(ar)}')
    print(f'Средний рост: {sum(ar)/len(ar)}')
