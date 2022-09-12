from datetime import datetime, timedelta

dd, st_t, end_t = datetime.strptime(input(),'%d.%m.%Y %H:%M'), 9, 21
if dd.weekday() >4:
    st_t, end_t = 10, 18
if timedelta(hours=dd.hour, minutes=dd.minute, seconds=dd.second).total_seconds() >= timedelta(hours=st_t).total_seconds() and timedelta(hours=dd.hour, minutes=dd.minute, seconds=dd.second).total_seconds() < timedelta(hours=end_t).total_seconds():
    print(int((timedelta(hours=end_t).total_seconds() - timedelta(hours=dd.hour, minutes=dd.minute, seconds=dd.second).total_seconds())/60))
else:
    print('Магазин не работает')