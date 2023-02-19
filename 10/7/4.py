with open('data.csv', 'r', encoding='UTF-8') as file:
    file_lines = (line for line in file)
    values = (l.rstrip().split(',') for l in file_lines)
    next(values)
    _filtered_list = (int(f[1]) for f in values if f[2] == 'a')
    print (sum(_filtered_list))