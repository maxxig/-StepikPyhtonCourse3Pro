import csv

with open('prices.csv', encoding='utf-8') as file_in:
    data_reader = csv.DictReader(file_in, delimiter=';')
    data = [d for d in data_reader]
    products = []

    for d in data:
        store = d['Магазин']
        d.pop('Магазин')
        for item in d.items():
            products.append([store, item[0], item[1]])
    # print(products)
    min_price = min(products, key=lambda x:float(x[2]))[2]

    products = sorted(list(filter(lambda x: x[2] == min_price, products)), key=lambda y: (y[1],y[0]))

    print(f'{products[0][1]}: {products[0][0]}')