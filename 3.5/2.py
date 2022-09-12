from datetime import datetime, timedelta

my_dcit = dict()
d = datetime.strptime('01.01.0001', '%d.%m.%Y')
stop_d = datetime.strptime('31.12.9999', '%d.%m.%Y')

while(d < stop_d):
    if d.day == 13:
        if d.weekday() in my_dcit:
            my_dcit[d.weekday()] += 1
        else:
            my_dcit[d.weekday()] =1
    d += timedelta(days=1)
sorted(my_dcit)
print(*[s for i, s in sorted(my_dcit.items())], sep='\n')