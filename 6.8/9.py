import csv, json
from collections import Counter
data = []
cn = Counter()
for i in range (1,5):
    with open(f"quarter{i}.csv", "r", encoding='utf-8') as f:
        cn = cn + Counter({d[0]: int(d[1])+int(d[2])+int(d[3]) for i, d in enumerate(csv.reader(f)) if i != 0})
#print(cn)
with open("prices.json", "r", encoding='utf-8') as pr_f:
    prices = json.load(pr_f)

total = 0
for i, v in cn.items():
    total += prices.get(i) * v

print(total)