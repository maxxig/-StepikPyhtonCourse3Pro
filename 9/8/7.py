import functools

def strip_range(start, end, char = '.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [v for v in func(*args, **kwargs)]
            for i in range(start, end):
                if i >= 0  and i < len(res):
                    res[i] = char
            return ''.join(res)
        return wrapper
    return decorator


@strip_range(100, 200, '=')
def beegeek():
    return 'beegeek'


print(beegeek())