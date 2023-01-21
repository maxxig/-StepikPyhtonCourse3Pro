import json

with open('countries.json') as input_file:
    data = json.load(input_file)

result_dict = {}

for item_data in data:
    if item_data['religion'] not in result_dict:
        result_dict[item_data['religion']] = [item_data['country']]
    else:
        result_dict[item_data['religion']].append(item_data['country'])

with open('religion.json', 'w') as output_file:
    json.dump(result_dict, output_file, indent='   ')