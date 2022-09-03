from datetime import date, datetime, timedelta

def date_convert_to_set(arr):
    _set = set()
    for bd in arr:
        if len(bd) <= 10:
            _set.add(datetime.strptime(bd,'%d.%m.%Y'))
        else:
            sd = datetime.strptime(bd.split('-')[0],'%d.%m.%Y')
            ed = datetime.strptime(bd.split('-')[1],'%d.%m.%Y')
            while(sd<=ed):
                _set.add(sd)
                sd += timedelta(days=1)
    return _set

def is_available_date(booked_dates , date_for_booking):
    booked_dates_set = date_convert_to_set(booked_dates)
    date_for_booking_set = date_convert_to_set([date_for_booking])
    if len(date_for_booking_set & booked_dates_set) == 0:
        return True
    return False


dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date))