import json

with open('people.json', encoding='utf-8') as input_file:
    data = json.load(input_file)

my_set = set()
for d in data:
    my_set.update(d.keys())


#my_dict = {s: None for s in my_set} var 1

my_dict = dict.fromkeys(my_set, None)
for i, d in enumerate(data):
    append_result = my_dict.copy()
    append_result.update(d)
    data[i] = append_result

with open('updated_people.json', 'w') as output_file:
    json.dump(data, output_file, indent='   ')