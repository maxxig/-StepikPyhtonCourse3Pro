import calendar
from datetime import datetime, timedelta, date

def get_days_in_month(y, m):
    mt = datetime.strptime(m, '%B').month
    end_day = calendar.monthrange(y, mt)[1]
    return [date(y, mt, i+1) for i in range(end_day)]

#print(get_days_in_month(2021, 'December'))
print(get_days_in_month(1957, 'July'))