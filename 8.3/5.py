def get_pow(a, n):
    def rec(a, step = n):
        if step == 1:
            return a
        if step == 0:
            return 1
        else:
            return a * rec(a, step-1)
    return rec(a)


print(get_pow(99, 0))