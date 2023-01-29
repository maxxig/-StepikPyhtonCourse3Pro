class Fibonacci:
    def __init__(self):
        self.minus_1 = 1
        self.minus_2 = 1
        self.cnt = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.cnt <2:
            self.cnt += 1
            return 1
        else:
            res = self.minus_1 + self.minus_2
            self.minus_2 = self.minus_1
            self.minus_1 = res
            return res


fibonacci = Fibonacci()

for _ in range(100):
    next(fibonacci)

print(next(fibonacci))