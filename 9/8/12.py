import functools
class MaxRetriesException(Exception):
    pass
def retry(times: int):
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res, i = None, 0
            while(i<times):
                try:
                    res = func(*args, **kwargs)
                except:
                    i+=1
                    continue
                else:
                    break
            if res == None and i >= times:
                raise MaxRetriesException
            return res
        return wrapper

    return decor


@retry(5)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')


try:
    beegeek()
except Exception as e:
    print(type(e))