import csv
from collections import Counter

with open("name_log.csv", "r", encoding='utf-8') as f:
    data = [c[1] for c in csv.reader(f)]
del data[0]
cn = Counter(data)
for k, v in {k:v for k,v in sorted(cn.items(), key = lambda x:x[0])}.items():
    print(f"{k}: {v}")

