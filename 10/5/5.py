from datetime import date, timedelta
def dates(start, count = None):
    cnt = 1
    while(1):
        if (count is None and start >= date(9999,12,31)):
            yield start
            return
        elif count is not None and cnt > count:
            return
        yield start
        cnt += 1
        start += timedelta(days=1)

generator = dates(date(2049, 1, 7))

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))