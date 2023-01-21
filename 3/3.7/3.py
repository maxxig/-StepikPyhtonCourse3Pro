import calendar
from datetime import datetime

d = datetime.strptime(input(),'%Y-%m-%d')
print(list(calendar.day_name)[d.weekday()])