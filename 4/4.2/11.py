import csv

def condense_csv(filename, id_name):
    data, data_dict, column, result = [],{}, [id_name], []
    with open(filename, encoding='utf-8') as file:
        data = [list(d) for d in csv.reader(file)]
    for d in data:
        if d[1] not in column:
            column.append(d[1])
        if d[0] not in data_dict:
            data_dict[d[0]] = {d[1]:d[2]}
        else:
            data_dict[d[0]][d[1]] = d[2]

    for dd in data_dict.items():
        temp = [dd[0]]
        for i in range(1, len(column)):
            temp.append(dd[1][column[i]])
        result.append(temp)

    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        write = csv.writer(file)
        write.writerow(column)
        write.writerows(result)

condense_csv(filename ='11.csv', id_name ='ID2')