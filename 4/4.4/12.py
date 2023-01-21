import json, csv

with open('students.json', encoding='utf-8') as input_file:
    data_reader = json.load(input_file)
    data = [d for d in data_reader]

data = list(map(lambda y:[y['name'], y['phone']], list(filter(lambda x:x['age'] >=18 and x['progress']>=75, data))))

data = sorted(data, key = lambda x:x[0])

with open('data.csv', 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['name','phone'])
    writer.writerows(data)