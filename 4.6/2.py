import pickle, sys

func_name, *args = [s.rstrip() for s in sys.stdin]

def func(*args):
    return ' '.join(args)

with open(func_name, 'rb') as file:
    f = pickle.load(file)

print(f(*args))
