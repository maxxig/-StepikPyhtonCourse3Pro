def starmap(func, data):
    _it = iter(data)
    return map(lambda x: func (*iter(x)), (i for i in _it))


points = [[10], [-9], [2]]

print(*starmap(lambda x: x ** 2, points))