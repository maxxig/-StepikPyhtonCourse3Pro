import functools
def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res+string if to_the_end else string+res
        return wrapper

    return decorator


@prefix('online-school ')
def make_lower(string, lower=True):
    '''makes string upper or lower'''
    if lower:
        return string.lower()
    return string.upper()


print(make_lower.__name__)
print(make_lower.__doc__)
print(make_lower('beegeek', False))