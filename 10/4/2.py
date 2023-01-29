class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt >= self.times:
            raise StopIteration
        else:
            self.cnt += 1
            return self.obj

repeater = BoundedRepeater((1, 2, 3, 4), 15)

for _ in range(10):
    next(repeater)

next(repeater)
next(repeater)
next(repeater)
next(repeater)
next(repeater)

try:
    print(next(repeater))
except StopIteration:
    print('Error')