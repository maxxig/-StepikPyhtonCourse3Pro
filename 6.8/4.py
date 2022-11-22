from collections import Counter, defaultdict

inp_str = input().split()
d_dict = defaultdict(int)

for i in inp_str:
    d_dict[len(i)] += 1

for x in (sorted(d_dict.items(), key=lambda x:x[1])):
    print(f"Слов длины {x[0]}: {x[1]}")
