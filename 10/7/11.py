def pairwise(iterable):
    _it = iter(iterable)
    try:
        _prev = next(_it)
    except:
        return
    for i in _it:
        yield (_prev, i)
        _prev = i
    yield (_prev, None)



# TEST_8:
print(list(pairwise([])))