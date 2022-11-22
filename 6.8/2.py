from collections import Counter

cn = Counter([s.lower() for s in input().split()])

min_value = cn.most_common()[-1][1]
min_dict = { k: v for k, v in cn.items() if v == min_value}
res = sorted([k for k in min_dict])
print(*res, sep = ', ')