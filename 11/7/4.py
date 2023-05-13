import re
in1 = input()
in2 = input()

f1 = re.search('.*[sz]e',in1, flags=re.IGNORECASE)
f_string = f'{f1.group()[:-2]}ze'
f_string2 = f'{f1.group()[:-2]}se'
print(f_string,f_string2)

if f1:
    res = re.findall(r'\b'+f_string+r'\b', in2, flags=re.IGNORECASE)
    res2 = re.findall(r'\b'+f_string2+r'\b', in2, flags=re.IGNORECASE)
    print(len(res)+len(res2))
else:
    print('0')