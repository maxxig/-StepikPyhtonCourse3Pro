import json
from collections import ChainMap

with open("zoo.json","r", encoding='utf-8') as file:
    data = json.load(file)

print(sum(ChainMap(*data).values()))