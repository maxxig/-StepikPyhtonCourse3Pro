from datetime import datetime

n = int(input())
res = dict()
for _ in range(n):
    d = datetime.strptime(input().split()[2],'%d.%m.%Y')
    if d not in res:
        res[d] = 1
    else:
        res[d] += 1
max_cnt = res[max(res, key=res.get)]
for k in sorted({k: r for k,r in res.items() if r == max_cnt}):
    print(datetime.strftime(k, '%d.%m.%Y'))