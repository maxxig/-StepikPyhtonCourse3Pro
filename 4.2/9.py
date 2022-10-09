import csv
from datetime import datetime

data, data_dict = [], {}

with open('name_log.csv', encoding='utf-8') as file:
    data = [list(d) for d in csv.reader(file)]
columns = data[0]
del data[0]

for d in data:
    if d[1] not in data_dict:
        data_dict[d[1]] = [d[0], d[2]]
    else:
        old_date = datetime.strptime(data_dict[d[1]][1], '%d/%m/%Y %H:%M')
        new_date = datetime.strptime(d[2], '%d/%m/%Y %H:%M')
        if new_date >= old_date:
            data_dict[d[1]] = [d[0], d[2]]
return_data = [[s[1][0], s[0], s[1][1]] for s in sorted(data_dict.items(), key=lambda x: x[0])]

with open('new_name_log.csv', 'w',  encoding='utf-8', newline='') as file:
    write = csv.writer(file)
    write.writerow(columns)
    write.writerows(return_data)
