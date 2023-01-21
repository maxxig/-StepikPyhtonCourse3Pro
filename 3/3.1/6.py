import datetime
from datetime import date
def get_date_range(start_date, end_date):
    res = []
    if end_date >= start_date:
        res.append(start_date)
        tmp_date = start_date
        while(tmp_date < end_date):
            tmp_date = tmp_date + datetime.timedelta(days=1)
            res.append(tmp_date)
    return res

date1 = date(2019, 6, 5)
date2 = date(2022, 6, 6)
print(len(get_date_range(date1, date2)))