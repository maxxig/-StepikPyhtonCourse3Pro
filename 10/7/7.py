def txt_to_dict():
    with open('planets.txt', 'r', encoding='UTF-8') as file:
        pl_list = (p.rstrip().split('\n') for p in file)
        tmp = dict()
        for p in pl_list:
            if p[0] == '':
                res = tmp.copy()
                yield res
                tmp.clear()
            else:
                val = p[0].split('=')
                tmp[val[0].rstrip()] = val[1].lstrip()
        yield tmp



planets = txt_to_dict()

print(*planets)