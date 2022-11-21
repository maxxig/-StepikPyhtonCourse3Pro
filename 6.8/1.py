from collections import Counter

cn = Counter([s.lower() for s in input().split()])

print(cn.most_common()[0][0])