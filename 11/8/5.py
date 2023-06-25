import re

s = input()
def func(match_obj):
    return match_obj.group(2) * int(match_obj.group(1))

while(1):
    if (re.search(r'(\d{1,})\((\w+)\)', s) is None):
        break
    else:
        s = re.sub(r'(\d{1,})\((\w+)\)', func, s)
#res = re.search(r'(\d{1,})\((\w+)\)', s)
print(s)