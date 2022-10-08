import sys
db, subj = [], None

for line in sys.stdin:
    line_split = line.split('/')
    if len(line_split) == 1:
        subj = line_split[0].rstrip()
    else:
        db.append((line_split[0].rstrip(), line_split[1].rstrip().lstrip(),line_split[2].lstrip().rstrip()))

res = sorted(list(filter(lambda x: x[1] == subj, db)) , key= lambda y : (y[2],y[0]))

print(*[r[0] for r in res], sep = '\n')