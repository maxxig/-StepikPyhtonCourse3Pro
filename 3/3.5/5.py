from datetime import datetime

n = int(input())
res = dict()
for _ in range(n):
    fio = input().split()
    d = datetime.strptime(fio[2],'%d.%m.%Y')
    if d not in res:
        res[d] = dict(name = f'{fio[0]} {fio[1]}', cnt = 1)
    else:
        res[d]['cnt'] += 1
min_date = min(res)
if res[min_date]['cnt'] == 1:
    print(f'{datetime.strftime(min_date, "%d.%m.%Y")} {res[min_date]["name"]}')
else:
    print(f'{datetime.strftime(min_date, "%d.%m.%Y")} {res[min_date]["cnt"]}')