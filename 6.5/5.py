from collections import defaultdict

def flip_dict(dict_of_lists):
    dict_result = defaultdict(list)
    for k,values in dict_of_lists.items():
        for v in values:
            dict_result[v].append(k)
    return dict_result

# print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
data = {6: [1, 2, 3], 88: [3, 4, 6], '99': ['a', 'f', '3', 1, 2, 3], 'a': [1, 2, 3]}

print(flip_dict(data))