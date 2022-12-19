def recursive_sum(a, b):
    def rec(step = 0):
        if step == a:
            return b
        else:
            return 1 + rec(step+1)

    return rec()

print(recursive_sum(62, 62))