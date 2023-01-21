def func(number):
    str_number = str(number)
    def rec(number, step=0):
        if step < len(number):
            return int(number[step]) + rec(number, step + 1)
        else:
            return 0
    return rec(str_number)


print(func(int(input())))