def get_value(nested_dicts,key):
    if type(nested_dicts) == dict and key in nested_dicts:
        return nested_dicts[key]
    if type(nested_dicts) == dict and key not in nested_dicts:
        for k, v in nested_dicts.items():
            if type(v) == dict:
                val = get_value(v, key)
                if val is not None:
                    return val



data = {'a': 11, 'b': {'c': 34, 'd': 2224, 'e': {'f': 5133, 'g': 609, 'z': {'y': {'res': 100}}}}}

print(get_value(data, 'res'))