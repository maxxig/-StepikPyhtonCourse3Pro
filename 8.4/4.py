def get_all_values(nested_dicts,key):
    my_set = set()
    for k, v in nested_dicts.items():
        if type(v) == dict:
            #val = get_all_values(v, key)
            my_set.update(get_all_values(v, key))
        elif key in nested_dicts and key == k:
            my_set.update(set([nested_dicts.get(key)]))
    return my_set




my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
print(type(result))

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))