def around(iterable):
    _it = iter(iterable)
    _prev = None
    try:
        _current = next(_it)
    except:
        return
    for i in _it:
        yield (_prev,_current, i)
        _prev = _current
        _current = i
    yield (_prev,_current, None)

# TEST_3:
iterator = around(iter('beegeek'))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_4:
data = map(abs, range(-100, 100))

print(*around(data))

# TEST_5:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*around(data))

# TEST_6:
data = map(str.upper, 'y')

iterator = around(data)

print(next(iterator))

# TEST_7:
data = map(str.upper, 'yt')

print(*around(data))

# TEST_8:
data = map(str.upper, 'ytu')

print(*around(data))

# TEST_9:
data = ['bee', 'geek', 'stepik', 'python']

print(*around(data))

# TEST_10:
print(list(around([])))