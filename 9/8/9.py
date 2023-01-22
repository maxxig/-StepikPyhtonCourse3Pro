import functools

def takes(*args_t):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for a in args:
                if type(a) not in args_t:
                    raise TypeError
            for k in kwargs.values():
                if type(k) not in args_t:
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator


@takes(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], 3))
except TypeError as e:
    print(type(e))