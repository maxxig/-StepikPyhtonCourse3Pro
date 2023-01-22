import functools
def takes_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for a in args:
            if type(a) != int:
                raise TypeError
            elif a<=0:
                raise ValueError
        for k in kwargs.values():
            if type(k) != int:
                raise TypeError
            elif k<=0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper


@takes_positive
def power(a, n):
    return a ** n


try:
    print(power(a="3", n="2"))
except Exception as err:
    print(type(err))