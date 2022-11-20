from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

new_data = OrderedDict()

for i in range(len(data)):
    el = data.popitem(False)
    new_data[el[0]] = el[1]
    el = data.popitem(True)
    new_data[el[0]] = el[1]
    if len(data) == 0:
        break

print(new_data)