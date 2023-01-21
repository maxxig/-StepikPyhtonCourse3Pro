import csv
data, data_dict = [], {}
with open('titanic.csv', encoding='utf-8') as file:
    data = [list(d) for d in csv.reader(file, delimiter=';')]

del data[0]
data = list(filter(lambda x: x[0] == '1' and float(x[3])<18, data))
data = list(map(lambda x: x[1], sorted(data, key = lambda x: x[2], reverse=True)))
print(*data, sep ='\n')
