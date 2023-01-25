import functools
def ignore_exception(*args_d, **kwargs_d):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                if e.__class__ in args_d or e.__class__ in kwargs_d.values():
                    print(f"Исключение {e.__class__.__name__} обработано")
                else:
                    raise e.__class__
            else:
                return res
        return wrapper
    return decorator


@ignore_exception(TypeError)
def func():
    '''func docs'''
    raise ValueError


try:
    func()
except Exception as e:
    print(type(e))