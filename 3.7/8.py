import calendar
from datetime import datetime, timedelta, date

_year = int(input())

def get_first_date(y, m, d):  #d - day of week
    dt = datetime(year=y,month=m,day=1)
    while(dt.weekday()!=d):
        dt += timedelta(days=1)
    return dt.day
cnt = 1
res = []

for _m in range(1,13):
    _day_first = get_first_date(_year,_m, 3)
    cnt = 0
    for _d in range(_day_first, calendar.monthrange(_year, _m)[1], 7):
        cnt += 1
        if(cnt == 3):
            res.append(date(_year,_m,_d))
sorted(res)
for a in res:
    print(datetime.strftime(a, '%d.%m.%Y'))