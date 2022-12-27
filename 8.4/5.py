def dict_travel(nested_dicts):
    def rec(nested_dicts):
        my_dict = {}
        for k, v in nested_dicts.items():
            if type(v) == dict:
                temp_dict = rec(v)
                for temp_k, temp_v in temp_dict.items():
                    my_dict[k+'.'+temp_k] = temp_v
            else:
                my_dict[k] = v
        return my_dict
    result = list(sorted(rec(nested_dicts).items(), key= lambda x: x[0]))
    for r in result:
        print(f"{r[0]}: {r[1]}")



data = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},'address': {'streetaddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'}, 'postalcode': '125315'}}

dict_travel(data)