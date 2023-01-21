import csv
data, data_dict, columns = [], {}, ['domain','count']
with open('data.csv', encoding='utf-8') as file:
    data = [d[0].split(',')[2] for d in csv.reader(file, delimiter=';')]

del data[0]

data = list(map(lambda x: x.split('@')[1], data))
for d in data:
    if d not in data_dict:
        data_dict[d] = 1
    else:
        data_dict[d] += 1
data_dict = [list(s) for s in sorted(data_dict.items(), key=lambda x: (x[1],x[0]))]

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    write = csv.writer(file)
    write.writerow(columns)
    write.writerows(data_dict)
