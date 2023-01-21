from collections import Counter
import sys

data = Counter({d[0]:int(d[1]) for d in [d.split() for d in [line.strip() for line in sys.stdin]]})
print(data.most_common()[-2][0])
