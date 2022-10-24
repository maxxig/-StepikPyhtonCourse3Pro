import json
from datetime import datetime, time
start_time, end_time = datetime.strptime('10:00','%H:%M').time(), datetime.strptime('12:00','%H:%M').time()


with open('pools.json', encoding='utf-8') as input_file:
    data_reader = json.load(input_file)
    data = [d for d in data_reader]

def data_filter(item):
    time_period =  item['WorkingHoursSummer']['Понедельник'].split('-')
    start, end = datetime.strptime(time_period[0],'%H:%M').time(), datetime.strptime(time_period[1],'%H:%M').time()
    if (end>=start and start<=start_time and end_time<=end):
        return True
    return False

data =  [d for d in data if data_filter(d) == True]
data = sorted(data, key=lambda x: (-x['DimensionsSummer']['Length'],-x['DimensionsSummer']['Width']))

print(f"{data[0]['DimensionsSummer']['Length']}x{data[0]['DimensionsSummer']['Width']}")
print(f"{data[0]['Address']}")
