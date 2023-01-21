def print_given(*args, **kwargs):
    for a in args:
        print(f'{a} {type(a)}')
    for k, v in sorted(kwargs.items()):
        print(f'{k} {v} {type(v)}')

print_given(1, [1, 2, 3], 'three', two=2)
print_given('apple', 'cherry', 'watermelon')
print_given(b=2, d=4, c=3, a=1)
print_given()