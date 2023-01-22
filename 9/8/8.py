import functools
def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if type(res) == datatype:
                return res
            else:
                raise TypeError
        return wrapper
    return decorator


@returns(int)
def add(a, b):
    return a + b

print(add(a=10, b=5))