import csv
data, data_dict = [], {}
with open('wifi.csv', encoding='utf-8') as file:
    data = [list((d[1],d[3])) for d in csv.reader(file, delimiter=';')]

del data[0]

for d in data:
    if d[0] not in data_dict:
        data_dict[d[0]] = int(d[1])
    else:
        data_dict[d[0]] += int(d[1])

data_dict = [list(s) for s in sorted(data_dict.items(), key=lambda x: (-x[1], x[0]))]
print(*[f'{d[0]}: {d[1]}' for d in data_dict], sep='\n')
