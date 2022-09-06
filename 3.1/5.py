from datetime import date
dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]

def get_min_max(dates):
    if len(dates) == 0:
        return tuple()
    return (min(dates), max(dates))
print(get_min_max(dates))
print(get_min_max([]))