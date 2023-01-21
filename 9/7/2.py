import functools
orig_print = print
def new_print(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = list(map(lambda x:str(x).upper(), args))
        kwargs = {k: str(v).upper() for (k, v) in kwargs.items()}
        return orig_print(*args, **kwargs)
    return wrapper
print = new_print(orig_print)


print('aaa', 'bbb', 'CCC', sep='xxx', end='stepik')
print('aaa', 'bbb', 'CCC', sep='--', end='python')
print('aaa', 'bbb', 'CCC', sep='qqq', end='!')