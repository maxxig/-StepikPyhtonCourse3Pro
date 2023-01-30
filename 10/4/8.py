class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.it=iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.it)
        except:
            self.it = iter(self.iterable)
            return next(self.it)

cycle = Cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for _ in range(100):
    print(next(cycle))