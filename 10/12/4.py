from collections import namedtuple
import itertools

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

input_int = int(input())

finded_price = 0
finded_list = None

for i in range(1, len(items)+1):
    _comb = itertools.combinations(items, i)
    for c in _comb:
        _list = list(c)
        if(sum([l.mass for l in _list])) <= input_int:
            _goal = sum([l.price for l in _list])
            if _goal > finded_price:
                finded_price = _goal
                finded_list = _list

if finded_list is None:
    print('Рюкзак собрать не удастся')
else:
    print(*[f"{l.name}" for l in sorted(finded_list, key=lambda x: x.name)], sep='\n')