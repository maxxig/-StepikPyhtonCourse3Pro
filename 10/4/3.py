class Square():
    def __init__(self, n):
        self.n = n
        self.c_number = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.c_number >= self.n:
            raise StopIteration
        else:
            self.c_number += 1
            return self.c_number * self.c_number

squares = Square(2)

try:
    print(next(squares))
    print(next(squares))
    print(next(squares))
except:
    print('Error')