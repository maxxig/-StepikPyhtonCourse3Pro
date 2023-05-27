import re,sys
# text = ''.join([line.rstrip() for line in sys.stdin])
text = '''<p><a href="https://stepik.org" arara="sdasd">Stepik</a></p>
<div class="catalog"><a href="https://stepik.org/catalog">Study hard. Teach harder</a></div>'''

tags = re.findall(r'<([^/][a-zA-Z0-9-/ :\.\="]*?)>', text)
# print(tags)

for t in tags:
    r = t.split()
    tg = r[0]
    # print(tg)
    s = [re.match(r'([\w-]*)="[a-zA-Z0-9-/:\.\"]*"', i).group(1) for i in r[1:]]
    print(s)
    s.sort()
    print(s)
    # att = ', '.join([re.match(r'([\w-]*)="[a-zA-Z0-9-/:\.\"]*"', i).group(1) for i in r[1:]])
    # for i in r[1:]:
    #     att = att + ', ' + re.match(r'([\w-]*)="[a-zA-Z0-9-/:\.\"]*"', i).group(1)
        # print(att)
        #print(att.group(1))
    # print(tg + ": " + att)