import calendar
try:
    s = {i: name for i, name in enumerate([n for n in calendar.month_name if n != ''], 1)}
    print(s[int(input())])
except KeyError:
    print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')