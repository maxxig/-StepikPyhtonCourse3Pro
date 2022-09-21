import calendar
from datetime import datetime
d = input().split()
m = datetime.strptime(d[1], '%b').month
print(calendar.month(int(d[0]), m))