from itertools import groupby
def group_anagrams(words):
    _words = sorted(words, key=lambda x: sorted(list(x)))
    _words = groupby(_words, key=lambda y: sorted(list(y)))
    return [tuple(v) for k, v in _words]

# TEST_4:
groups = group_anagrams(['чулки', 'чулки', 'чулки', 'чулки', 'чулки', 'чулки', 'чулки'])

print(*groups)

# TEST_5:
groups = group_anagrams(['beegeek'])

print(*groups)

# TEST_6:
groups = group_anagrams(['клоун', 'отсечка', 'кулон', 'уклон', 'чесотка', 'чулки', 'яяя', 'чулки', 'чесотка', 'яяя'])

print(*groups)

# TEST_7:
groups = group_anagrams(['клоун', 'яяя', 'жжж', 'бббб', 'кулон'])

print(*groups)
