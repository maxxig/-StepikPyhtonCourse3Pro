import re
s = input()
_t = re.findall("7{1}-\d{3}-\d{3}-\d{2}-\d{2}", s)
_t.extend(re.findall("8{1}-\d{3}-\d{4}-\d{4}", s))
print(*_t, sep='\n')