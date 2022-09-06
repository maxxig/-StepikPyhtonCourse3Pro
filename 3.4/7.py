from datetime import datetime, timedelta

dd = datetime.strptime(input(),'%d.%m.%Y')
d = 2
print(datetime.strftime(dd, '%d.%m.%Y'))
for _ in range(9):
    dd += timedelta(days=d)
    print(datetime.strftime(dd, '%d.%m.%Y'))
    d += 1