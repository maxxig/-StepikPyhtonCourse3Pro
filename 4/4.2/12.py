import csv

with open('student_counts.csv', encoding='utf-8') as file_in:
    data_reader = csv.DictReader(file_in)
    data = [d for d in data_reader]

    columns = data_reader.fieldnames
    save_y = columns[0]
    del columns[0]
    columns = sorted(columns, key=lambda x: (int(x.split('-')[0]),x.split('-')[1]))
    columns.insert(0,save_y)
    result = []
    for d in data:
        temp = []
        for c in columns:
            temp.append(d[c])
        result.append(temp)

    with open('sorted_student_counts.csv', 'w',  encoding='utf-8', newline='') as file_out:
        write = csv.writer(file_out)
        write.writerow(columns)
        write.writerows(result)