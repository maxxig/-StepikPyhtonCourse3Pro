from itertools import product
def password_gen():
    # for i in range(10):
    #     for j in range(10):
    #         for k in range(10):
    #             yield str(i) + str(j) + str(k)
    for p in product(range(10), repeat=3):
        yield f'{p[0]}{p[1]}{p[2]}'

passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))