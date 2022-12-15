import calendar, locale
locale.setlocale(locale.LC_ALL,'ru_RU.UTF-8')
def get_weekday(number):
    if  type(number) != int:
        raise TypeError('Аргумент не является целым числом')
    elif number < 1 or number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return calendar.day_name[number-1].capitalize()


try:
    print(get_weekday({}))
except Exception as err:
    print(err)
    print(type(err))