en = set("AaBCcEeHKMOoPpTXxy".lower())
ru = set("АаВСсЕеНКМОоРрТХху".lower())
ru_cnt, en_cnt = 0,0

for _ in range(3):
    s = set(input().lower())
    if s.issubset(ru):
        ru_cnt +=1
    if s.issubset(en):
        en_cnt +=1
if ru_cnt == 3:
    print('ru')
elif ru_cnt == 1 or ru_cnt == 2:
    print('mix')
else:
    print('en')