def sourcetemplate(url):
    def func(**kwargs):
        nonlocal url
        keys = [f"{k}={v}" for k, v in kwargs.items()]
        keys.sort()
        url2 = '&'.join(keys)
        return '?'.join([url, url2]) if len(url2)>0 else url
    return func

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load())

url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))

url = 'https://hide_and_seek.harvard'
load = sourcetemplate(url)
print(load(wizard='Dambldor', magic_wand='elderberry', thief='Volandemord'))