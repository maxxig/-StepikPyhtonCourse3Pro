import csv, json
from datetime import datetime

with open ('exam_results.csv', encoding='utf-8') as input_file:
    data_reader = csv.DictReader(input_file, delimiter=',')
    data = [d for d in data_reader]

def get_best_result(item):
    name, surname, email = item['name'], item['surname'], item['email']
    filter_data = list(filter(lambda x: x['name'] == item['name'] and x['name'] == item['name'] and x['email'] == item['email'], data))
    return sorted(filter_data, key=lambda x: (x['score'], datetime.strptime(x['date_and_time'],'%Y-%m-%d %H:%M:%S')), reverse=True)[0]

new_data = []
for d in data:
    best_result = get_best_result(d)
    if best_result not in new_data:
        new_data.append(best_result)

new_data = sorted(new_data, key=lambda x: x['email'])
for iten in new_data:
    iten['best_score'] = int(iten['score'])
    del iten['score']

with open('best_scores.json', 'w', encoding='utf-8') as output_file:
    json.dump(new_data, output_file, indent='   ', ensure_ascii=False)