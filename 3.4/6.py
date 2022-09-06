from datetime import datetime, timedelta
def num_of_sundays(y):
    d = datetime(year=y, month=1, day=1)
    while(d.weekday() != 6):
        d = d + timedelta(days=1)
    cnt = 0
    while(d.year == y):
        d = d + timedelta(days=7)
        cnt += 1
    return cnt

print(num_of_sundays(768))
