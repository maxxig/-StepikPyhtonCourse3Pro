import csv, json

with open ('playgrounds.csv', encoding='utf-8') as input_file:
    data_reader = csv.DictReader(input_file, delimiter=';')
    data = [d for d in data_reader]

result_dict = {}

for item_data in data:
    if item_data['AdmArea'] not in result_dict:
        result_dict[item_data['AdmArea']] = {item_data['District']:[item_data['Address']]}
    elif item_data['District'] not in result_dict[item_data['AdmArea']]:
        result_dict[item_data['AdmArea']][item_data['District']] = [item_data['Address']]
    else:
        result_dict[item_data['AdmArea']][item_data['District']].append(item_data['Address'])

with open('addresses.json', 'w', encoding='utf-8') as output_file:
    json.dump(result_dict, output_file, indent='   ', ensure_ascii=False)

