from datetime import date
def print_good_dates(dates):
    dt =  list(filter(lambda x: True if x.year == 1992 and (x.day + x.month) == 29 else False, dates))
    dt.sort()
    print(*list(map(lambda x: x.strftime('%B %d, %Y'), dt)), sep = '\n')

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
