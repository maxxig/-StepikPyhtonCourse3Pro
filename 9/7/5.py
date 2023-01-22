import functools
def exception_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = ()
        try:
            res = (func(*args, **kwargs),'Функция выполнилась без ошибок')
        except:
            res = (None, 'При вызове функции произошла ошибка')
        return res
    return wrapper


@exception_decorator
def f(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(f(1, 2, 3, param1=4, param2='10'))