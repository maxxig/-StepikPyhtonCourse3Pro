import random
class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.current_n = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_n += 1
        if self.current_n > self.n:
            raise StopIteration
        else:
            return random.randint(self.left, self.right)



iterator = RandomNumbers(-1000, -900, 1)

print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')