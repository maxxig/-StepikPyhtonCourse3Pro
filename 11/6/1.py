from re import search
import sys
for line in sys.stdin:
    m = search('(\d{1,3})([ -]{1})(\d{1,3})\\2(\d{4,10})', line)
    print(f"Код страны: {m.group(1)}, Код города: {m.group(3)}, Номер: {m.group(4)}")