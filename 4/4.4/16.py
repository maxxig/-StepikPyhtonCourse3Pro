import json

with open('food_services.json', encoding='utf-8') as input_file:
    data_reader = json.load(input_file)
    data = [d for d in data_reader]

result = {}
for d in data:
    if d['TypeObject'] not in result:
        result[d['TypeObject']] = {'Name': d['Name']}
        result[d['TypeObject']]['SeatsCount'] = d['SeatsCount']
    elif d['SeatsCount'] > result[d['TypeObject']]['SeatsCount']:
        result[d['TypeObject']]['SeatsCount'] = d['SeatsCount']
        result[d['TypeObject']]['Name'] = d['Name']
result = {k:v for k,v in sorted(result.items(), key=lambda x: x[0])}

for k,v in result.items():
    print(f"{k}: {v['Name']}, {v['SeatsCount']}")