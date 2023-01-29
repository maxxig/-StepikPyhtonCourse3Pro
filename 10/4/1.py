class Repeater:
    def __init__(self, text):
        self.text = text
    def __iter__(self):
        return self
    def __next__(self):
        return self.text


repeater = Repeater((1, 2, 3, 4))

for _ in range(55):
    print(next(repeater))