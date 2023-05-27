import re,sys
text = ''.join([line.rstrip() for line in sys.stdin])
res = re.findall(r'<a href="((https{0,1}:\/\/([a-zA-Z-]*\.){1,}[a-zA-Z-]*){0,1}\/{0,1}([a-zA-Z-]*\/|[a-zA-Z-]*){0,}\/{0,1})">(.*?)<\/a>', text, flags=re.S|re.DOTALL)
for i in res:
    print(i[0], i[-1], sep=', ')

