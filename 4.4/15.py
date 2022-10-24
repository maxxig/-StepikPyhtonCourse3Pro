import json

with open('food_services.json', encoding='utf-8') as input_file:
    data_reader = json.load(input_file)
    data = [d for d in data_reader]

district_data = {}
net_objects = []
for d in data:
    if d['District'] not in district_data:
        district_data[d['District']] = 1
    else:
        district_data[d['District']] += 1
    if d['IsNetObject'] == 'да':
        net_objects.append(d)

#print(district_data)
district = [f'{k}: {v}' for k,v in sorted(district_data.items(), key=lambda x:x[1], reverse=True)][0]
net_objects_count = {}
for n_o in net_objects:
    if n_o['OperatingCompany'] not in net_objects_count:
        net_objects_count[n_o['OperatingCompany']] = 1
    else:
        net_objects_count[n_o['OperatingCompany']] += 1
print(district)
oper_company = [f'{k}: {v}' for k,v in sorted(net_objects_count.items(), key=lambda x:x[1], reverse=True)][0]
print(oper_company)
