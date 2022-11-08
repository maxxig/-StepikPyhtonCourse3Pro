from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
animal_list = []
with open('data.pkl', 'rb') as file:
    animal_list = pickle.load(file)

for al in animal_list:
    for f, value in zip(Animal._fields, al):
        print(f"{f}: {value}")
    print()