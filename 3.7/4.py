import calendar
d = input().split()
print(calendar.monthrange(int(d[0]), int(d[1]))[1])