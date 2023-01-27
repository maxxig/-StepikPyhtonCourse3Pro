from copy import copy
def get_min_max(data):
    _data = iter(data)
    _min, _max = None, None
    try:
        _min = next(_data)
        _max = _min
    except:
        return None
    for i in _data:
        if i < _min:
            _min = i
        if i > _max:
            _max = i
    return _min, _max

data = iter(range(100_000_000))

print(get_min_max(data))