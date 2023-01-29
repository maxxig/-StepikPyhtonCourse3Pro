def is_iterable(obj):
    try:
        obj.__iter__()
    except:
        return False
    else:
        return True

for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(element, 'iterable: ', is_iterable(element))