import datetime
import sys
max_date, min_date = None, None

for l in sys.stdin:
    d = datetime.datetime.strptime(l.rstrip(), '%Y-%m-%d')
    if max_date is None:
        min_date, max_date = d, d
    if d < min_date:
        min_date = d
    if d > max_date:
        max_date = d
print((max_date - min_date).days)
