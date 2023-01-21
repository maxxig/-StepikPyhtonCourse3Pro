inp = input().split()
a, pr = [], []
for i in inp:
    if int(i) in a and int(i) not in pr:
        pr.append(int(i))
    else:
        a.append(int(i))
pr.sort()
print(*pr)