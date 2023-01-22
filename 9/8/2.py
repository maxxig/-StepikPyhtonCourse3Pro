import functools
def returns_string(func):
    @functools.wraps(func)
    def wrapper (*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) == str:
            return res
        else:
            raise TypeError
    return wrapper
@returns_string
def concat(*args, **kwargs):
    return "".join([*args, *kwargs.values()])

print(concat("Hello ", x="world", y="!!!"))
