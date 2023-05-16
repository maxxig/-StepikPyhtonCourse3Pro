import re
in1 = input()
in2 = input()
print(len(list(filter(lambda x: x == in2,list(filter(lambda x: len(x)>0,re.findall(r'\b\w*\b', in1)))))))

