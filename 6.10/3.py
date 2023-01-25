from collections import ChainMap

def get_value(cm, key, from_left = True):
    sort = 1
    if key not in cm:
        return None
    else:
        if from_left:
            sort = 1
        else:
            sort = -1
        for d in cm.maps[::sort]:
            if key in d:
                return d[key]

chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})

print(get_value(chainmap, 'name'))