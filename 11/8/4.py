import re
s = input()
def func(match_obj):
    s = list(match_obj.group(0))
    s[0] = match_obj.group(0)[1]
    s[1] = match_obj.group(0)[0]
    return ''.join(s)


res = re.sub('\w{2,}', func, s)
print(res)