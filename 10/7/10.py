def with_previous(iterable):
    prev = None
    for i in iterable:
        yield (i, prev)
        prev = i


# TEST_3:
print(*with_previous(map(abs, range(-100, 100))))

# TEST_4:
print(*with_previous(map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')))

# TEST_5:
print(*with_previous('JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'))

# TEST_6:
print(*with_previous('A'))

# TEST_7:
print(*with_previous('AB'))

# TEST_8:
gen = with_previous(['bee', 'geek', 'stepik', 'python'])

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# TEST_9:
print(list(with_previous('')))
