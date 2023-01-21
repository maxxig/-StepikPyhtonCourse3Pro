import csv

def csv_columns(file_name):
    with open(file_name, encoding='utf-8') as file:
        data = [s for s in csv.reader(file)]
        result = {}
        for i, t in enumerate(data[0]):
            all_values = []
            for d in range(1, len(data)):
                all_values.append(data[d][i])
            result[t] = all_values
        return result


print(csv_columns('exam.csv'))