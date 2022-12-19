def get_fast_pow(a, n):
    def rec(a, step = n):
        if step == 1:
            return a
        elif step == 0:
            return 1
        elif step % 2 == 0:
            return rec(a * a, step/2)
        else:
            return a * rec(a, step - 1)

    return rec(a, n)

print(get_fast_pow(2, 100))