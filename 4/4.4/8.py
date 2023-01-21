import json

with open('data1.json', encoding='utf-8') as file1:
    data1 = json.load(file1)

with open('data2.json', encoding='utf-8') as file2:
    data2 = json.load(file2)

data1.update(data2)

with open('data_merge.json', 'w') as output_file:
    json.dump(data1, output_file, indent='   ')