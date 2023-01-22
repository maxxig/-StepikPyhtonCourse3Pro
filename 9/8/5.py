import functools
def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            open_tag, close_tag = '<'+tag+'>', '</'+tag+'>'
            return open_tag + func(*args, **kwargs) + close_tag
        return wrapper
    return decorator


@make_html('mark')
@make_html('mark')
@make_html('mark')
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)