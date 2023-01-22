import functools
def reverse_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    return wrapper


@reverse_args
def operation(a, b, value=10):
    return a // b - value

print(operation(70, 70, value=70))