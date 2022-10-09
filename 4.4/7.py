import json

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)

print(data)
# for d in data:
#     print(type(d))

def convert (item):
    _t = type(item)
    if _t == str:
        item += '1'
    elif _t == int:
        item += 1
    elif _t == bool:
        item = not item
    elif _t == list:
        item *= 2
    elif _t == dict:
        item['newkey'] = None
    return item

data = list(filter(lambda x: x is not None, data))
data = list(map(lambda x: convert(x), data))

with open('')
print(data)