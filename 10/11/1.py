from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]


_t = groupby(sorted(persons, key = lambda x: x.height), key=lambda x: x.height)

for k, item in _t:
    print(f"{k}:", ', '.join(i.name for i in sorted(item, key=lambda x:x.name)))