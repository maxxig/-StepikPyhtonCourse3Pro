import calendar
from datetime import datetime, timedelta, date

def get_all_mondays(y):
    day = calendar.monthrange(y, 1)
    dt = datetime(year=y,month=1,day=1)
    while(dt.weekday() != 0):
        dt += timedelta(days=1)
    res = []
    while(dt.year == y):
        res.append(date(dt.year, dt.month, dt.day))
        dt += timedelta(days=7)
    sorted(res)
    return res

print(get_all_mondays(1989))