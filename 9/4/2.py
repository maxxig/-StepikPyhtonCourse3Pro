old_print = print
def print(*args, **kwargs):
    args = tuple(list(map(lambda x: x.upper() if type(x) == str else x, args)))
    kwargs = dict(map(lambda x: (x[0], x[1].upper()) if type(x[1]) == str else (x[0], x[1]), kwargs.items()))
    old_print(*args, **kwargs)

words = [['black', 'white', 'grey', 'black-1', 'white-1', 'python']]
print(*words, sep=' to ', end=' LOVE')