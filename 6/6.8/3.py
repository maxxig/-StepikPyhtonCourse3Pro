from collections import Counter

cn = Counter([s.lower() for s in input().split()])

max_value = cn.most_common()[0][1]

max_dict = { k: v for k, v in cn.items() if v == max_value}
res = sorted([k for k in max_dict])[-1]
print(res)