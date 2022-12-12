def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except:
        data[key] = [element]


data = {'a': [1, 2, 3]}

add_to_list_in_dict(data, 'a', 1)
add_to_list_in_dict(data, 'a', 3)
s=add_to_list_in_dict(data, 'b', False)

print(s)