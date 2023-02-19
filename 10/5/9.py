def flatten(nested_list):
    res = []
    def func(n_l):
        r_lisst = []
        if type(n_l) == int:
            r_lisst.append(n_l)
        else:
            for n in n_l:
                r_lisst.extend(func(n))
        return r_lisst

    yield from func(nested_list)


generator = flatten([[3, 2, 5345, 65, 7, 777, 0, 43, 65, 754, 3, 1, 2]])

print(*generator)