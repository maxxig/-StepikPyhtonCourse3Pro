import csv, datetime
from collections import namedtuple

Guest = namedtuple("Guest", ["surname", "name", "meeting_date_time"])
data = []


def get_date(_date, _time):
    d, t = [int(_d) for _d in _date.split('.')], [int(_t) for _t in _time.split(':')]
    return datetime.datetime(year=d[2], month=d[1], day=d[0], hour=t[0], minute=t[1])


with open("meetings.csv", "r", encoding='utf-8') as file:
    data_reader = csv.DictReader(file, delimiter=',')
    data = [Guest(d.get('surname'), d.get('name'), get_date(d.get('meeting_date'), d.get('meeting_time'))) for d in data_reader]

data = sorted(data, key=lambda x: x.meeting_date_time)

for d in data:
    print(d.surname, d.name)