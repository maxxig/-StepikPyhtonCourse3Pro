import calendar
from datetime import datetime
d = input().split()
m = datetime.strptime(d[1], '%B').month
print(calendar.monthrange(int(d[0]), m)[1])