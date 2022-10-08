import csv
data, data_dict = [], {}
with open('salary_data.csv', encoding='utf-8') as file:
    data = [d for d in csv.reader(file, delimiter=';')]

del data[0]

for d in data:
    if d[0] not in data_dict:
        data_dict[d[0]] = dict(salary = int(d[1]), count = 1)
    else:
        data_dict[d[0]]['salary'] = data_dict[d[0]]['salary'] + int(d[1])
        data_dict[d[0]]['count'] += 1

print(*dict(sorted(data_dict.items(), key= lambda x: x[1]['salary']/x[1]['count'])), sep = '\n')
