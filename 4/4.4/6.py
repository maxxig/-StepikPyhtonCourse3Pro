import json, sys

data = json.load(sys.stdin)

for key, item in data.items():
    if type(item) == list:
        print(f'{key}: {", ".join(str(x) for x in item)}')
    else:
        print(f'{key}: {item}')