from datetime import datetime, timedelta
def fill_up_missing_dates(dates):
    res_dates = []
    dt = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dates))
    max_d = max(dt)
    min_d = min(dt)
    while (min_d <= max_d):
        res_dates.append(datetime.strftime(min_d,'%d.%m.%Y'))
        min_d += timedelta(days=1)
    return res_dates

dates = ['20.07.2020', '16.05.2021', '19.01.2022', '18.11.2021', '17.10.2021', '15.03.2021']

print(fill_up_missing_dates(dates))