import pickle
from functools import reduce

pickle_file_name, nedomd5 = input(), int(input())
f = None
with open(pickle_file_name, 'rb') as file:
    f = pickle.load(file)

def sum(a, b):
    return a + b
file_nedomd5 = 0
if type(f) is dict:
    file_nedomd5 = reduce(sum, list(filter(lambda x: type(x) is int, [key for key in f])))
elif type(f) is list:
    data = list(filter(lambda x: type(x) is int, f))
    if len(data) > 0:
        file_nedomd5 = max(data) * min(data)
print('Контрольные суммы совпадают' if file_nedomd5 == nedomd5 else 'Контрольные суммы не совпадают')
