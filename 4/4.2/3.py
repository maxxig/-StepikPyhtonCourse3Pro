import csv
with open('sales.csv', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';')
    for i, d in enumerate(data):
        if i == 0:
            continue
        if int(d[1]) - int(d[2]) > 0:
            print(d[0])