import functools
def add_attrs(**kwargs_ext):
    def decorator(func):
        for k, v in kwargs_ext.items():
            func.__dict__[k] = v
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


@add_attrs(func_attr='i am attribute')
def func(a, b):
    '''func docs'''
    return


print(func.func_attr)