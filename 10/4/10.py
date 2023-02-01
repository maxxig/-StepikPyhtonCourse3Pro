class Alphabet:
    def __init__(self, language):
        if language == 'ru':
            self.start = 1072
            self.finish = 1103
            self.current = 1071
        if language == 'en':
            self.start = 97
            self.finish = 122
            self.current = 96
    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if (self.current > self.finish):
            self.current = self.start
        return chr(self.current)

ru_alpha = Alphabet('ru')

for _ in range(50):
    print(next(ru_alpha))