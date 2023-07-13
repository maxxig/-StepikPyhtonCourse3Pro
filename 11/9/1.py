import re
s = input()

result = re.split(r'[,;.]', s)

r = ' '.join(list(map(lambda x: x.strip(), result)))
print(r)