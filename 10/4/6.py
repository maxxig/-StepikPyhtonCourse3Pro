class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.it = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            t = next(self.it)
            return (t, self.data[t])
        except:
            raise StopIteration

data = {'Arthur': [100, 5], 'Timur': [100, 6], 'Dima': [100, 7, 8],
        'Anri': [100, 101], 'Roma': [99]}

pairs = DictItemsIterator(data)

print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')