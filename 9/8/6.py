import functools
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for i in range(times-1):
                func(*args, **kwargs)
            return res
        return wrapper
    return decorator


counter = 0


@repeat(10)
def beegeek():
    '''beegeek docs'''
    print('beegeek')


print(beegeek.__name__)
print(beegeek.__doc__)
beegeek()