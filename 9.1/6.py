def custom_isinstance(objects,typeinfo):
    res = 0
    for o in objects:
        if isinstance(o, typeinfo):
            res +=1
    return res

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))