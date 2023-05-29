import re
def func(obj):
    # print(obj.group().lower())
    return 'jpg' #obj.group().lower()
def normalize_jpeg(filename):
    return re.sub(r'([Jj]{1}[Pp]{1}[Ee]{0,1}[Gg]{1})$', func, filename)


print(normalize_jpeg('Это тест.JpEg'))