# from datetime import time
#
# alarm = time(7, 30, 25)
#
# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))


# from datetime import date
#
# birthday = date(1992, 10, 6)
#
# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))



# присваиваем самую раннюю дату урагана в переменную first_date
# from datetime import date
# florida_hurricane_dates = [date(1992, 10, 6)]
# first_date = min(florida_hurricane_dates)
#
# # конвертируем дату в ISO и RU формат
# iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
# ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
# us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')
#
# print(iso)
# print(ru)
# print(us)



from datetime import date

andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number