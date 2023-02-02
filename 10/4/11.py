class Xrange:
    def __init__(self, start, end, step = 1):
        self.start = start
        self.end = end
        self.step = step
        self.curent = start - step

    def __iter__(self):
        return self

    def __next__(self):
        self.curent += self.step
        if self.curent > self.end:
            raise StopIteration
        return self.curent


evens = Xrange(0, 10, 2)

print(*evens)