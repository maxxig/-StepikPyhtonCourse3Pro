from datetime import timedelta
from datetime import date
def saturdays_between_two_dates(date1, date2):
    res = 0
    start_date, end_date = min(date1, date2), max(date1, date2)
    tmp_date = start_date
    while(tmp_date <= end_date):
        if tmp_date.weekday() == 5:
            res += 1
        tmp_date += timedelta(days=1)
    return res


date1 = date(2012, 7, 11)
date2 = date(2011, 8, 16)
print(saturdays_between_two_dates(date1, date2))