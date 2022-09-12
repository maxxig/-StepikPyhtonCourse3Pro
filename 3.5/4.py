from datetime import datetime, timedelta
start_date = datetime.strptime(input(), '%d.%m.%Y')
end_date = datetime.strptime(input(), '%d.%m.%Y')
start_date_found = 0

while(start_date_found == 0):
        if(start_date.day + start_date.month) % 2 == 1:
            start_date_found = 1
        else:
            start_date += timedelta(days=1)

while(start_date <= end_date):
    if start_date.weekday() != 0 and start_date.weekday() != 3:
        print(datetime.strftime(start_date, '%d.%m.%Y'))
    start_date += timedelta(days=3)

