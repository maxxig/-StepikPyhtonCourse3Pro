import re,sys
text = ''.join([line.rstrip() for line in sys.stdin])
# text = '''<fieldset title="Search Python.org">
#     <span aria-hidden="true" class="icon-search"></span>
#     <label class="screen-reader-text" for="id-search-field">Search This Site</label>
#     <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">
#     <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
#         GO
#     </button>
# </fieldset>'''

tags = re.findall(r'<([^/][a-zA-Z0-9-/ :;#\.\="]*?)/{0,1}>', text)
# print(tags)
res = {}
for t in tags:
    r = t.split()
    tg = r[0]
    # print(tg)
    s = re.findall(r' ([a-zA-Z-]*?)="', t)
    # print(s)
    s.sort()
    if tg not in res:
        res[tg] = s
    else:
        for _s in s:
            if _s not in res[tg]:
                res[tg].append(_s)
res = sorted(res.items(), key=lambda x:x)
#print(res)
for r in res:
    if len(r) == 1:
        msg = r[0]+':'
    else:
        r[1].sort()
        msg = r[0] + ': ' + ', '.join(r[1])
    print(msg)