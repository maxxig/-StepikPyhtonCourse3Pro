from datetime import datetime, timedelta
input_date = datetime.strptime(input(), '%d.%m.%Y')

print(datetime.strftime((input_date - timedelta(days=1)),'%d.%m.%Y'))
print(datetime.strftime((input_date + timedelta(days=1)),'%d.%m.%Y'))