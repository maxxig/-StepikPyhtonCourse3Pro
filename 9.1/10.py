def zip_longest(*args, fill = None):
    result = []
    check = list(map(lambda x:True if len(x)>0 else False, args))
    if any(check):
        max_len = len(max(*args, key=lambda x: len(x)))
        for a in args:
            if len(a)< max_len:
                tmp = [fill] * (max_len-len(a))
                a.extend(tmp)
        result = list(zip(*args))
    return result

data = [[], ['one'], [], ['uno']]
print(zip_longest(*data))

# data = [[]]
# print(zip_longest(*data, fill='not known'))