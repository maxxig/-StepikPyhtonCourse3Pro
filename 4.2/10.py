import csv

data, column = [], int(input())-1

def my_sort(x):
    if x.isnumeric():
        return int(x)
    return x

with open('deniro.csv', encoding='utf-8') as file:
    data = [list(d) for d in csv.reader(file)]

data = sorted(data, key=lambda x: my_sort(x[column]))
print(*[f'{",".join(d)}' for d in data], sep='\n')