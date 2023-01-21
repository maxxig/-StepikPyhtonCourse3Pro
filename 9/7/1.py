import  functools
def sandwich(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res =  func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res
    return wrapper


@sandwich
def counter(*args, **kwargs):
    for i in args + tuple(kwargs.keys()) + tuple(kwargs.values()):
        print(i)

counter(10, 20, 30, sep='40', end='!!!', step='beegeek')