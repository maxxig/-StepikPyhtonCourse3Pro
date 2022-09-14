from datetime import datetime, timedelta

def choose_plural(num, tuple):
    if int(str(num)[-1]) in [0,5,6,7,8,9]:
        return f'{num} {tuple[2]}'
    if len(str(num))>1 and int(str(num)[-2:]) in [11,12,13,14]:
        return f'{num} {tuple[2]}'
    if int(str(num)[-1]) in [2,3,4]:
        return f'{num} {tuple[1]}'
    if int(str(num)[-1]) == 1:
        return f'{num} {tuple[0]}'

start_course = datetime(year=2022, month=11, day=8, hour=12, minute=00)
input_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')

delta = start_course - input_date

if delta.days < 0 or (delta.days == 0 and delta.seconds == 0):
    print('Курс уже вышел!')
elif delta.days == 0 and delta.seconds > 0:
    p1,p2,p3 = '','',''
    if delta.seconds // 3600 != 0:
        p1 = f'{choose_plural(delta.seconds // 3600, ("час", "часа", "часов"))}'
    if (delta.seconds // 60) % 60 != 0:
        p3 = f'{choose_plural((delta.seconds // 60) % 60, ("минута", "минуты", "минут"))}'
    if delta.seconds // 3600 != 0 and (delta.seconds // 60) % 60 != 0:
        p2 = ' и '
    print(f'До выхода курса осталось: {p1}{p2}{p3}')
else:
    p1 = choose_plural(delta.days, ('день', 'дня', 'дней'))
    p2 = ''
    if delta.seconds // 3600 != 0:
        p2 = f' и {choose_plural(delta.seconds // 3600, ("час", "часа", "часов"))}'
    print(f'До выхода курса осталось: {p1}{p2}')