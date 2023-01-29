def get_min_max(data):
    if len(data) == 0:
        return None
    min_iter, max_iter = enumerate(data),enumerate(data)
    _min, _max  = next(min_iter), next(max_iter)
    for i, _m in min_iter:
        if _m < _min[1]:
            _min = (i, _m)
    for i, _m in max_iter:
        if _m > _max[1]:
            _max = (i, _m)
    return _min[0], _max[0]



data = list(range(1, 101))[::-1]

print(get_min_max(data))