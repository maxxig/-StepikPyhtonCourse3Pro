from datetime import timedelta, date
def years_days(year):
    _date = date(year,1,1)
    while (_date < date(year+1,1,1)):
        yield _date
        _date = _date + timedelta(days=1)

# INPUT DATA:

# TEST_1:
dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))

# TEST_2:
dates = years_days(2077)

print(*dates)

# TEST_3:
dates = years_days(2000)

print(*dates)

# TEST_4:
dates = years_days(1900)

print(*dates)
