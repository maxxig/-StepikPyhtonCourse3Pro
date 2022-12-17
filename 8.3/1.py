def func(number):
    if number // 10 == 0:
        return 1
    else:
        return 1 + func(int(number/10))

print(func(int(input())))