from datetime import datetime, timedelta
arr = input().split()
res = []
for i, a in enumerate(arr):
    if i == 0:
        continue
    else:
        res.append(abs((datetime.strptime(a,'%d.%m.%Y') - datetime.strptime(arr[i-1],'%d.%m.%Y')).days))
print(res)


