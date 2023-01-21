from collections import Counter
cn = Counter(input().split(','))

for k, v in sorted(cn.items(), key=lambda x:x[0]):
    print(f"{k}: {v}")
