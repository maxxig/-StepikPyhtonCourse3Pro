import re
in1 = input()
in2 = input()
cnt = 0
for r in list(filter(lambda x: len(x)>0,re.findall(r'\b\w*\b', in1))):
    cnt += len(re.findall('\B'+in2+'\B', r))
print(cnt)
