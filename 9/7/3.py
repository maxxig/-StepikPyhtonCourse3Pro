import  functools
def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        res = func(*args, **kwargs)
        return res
    return wrapper


@do_twice
def beegeek():
    print('beegeek')


print(beegeek())