def to_binary(number):
    def rec(step = number):
        if step == 1:
            return '1'
        elif step == 0:
            return '0'
        else:
            return (str(step % 2) + str(rec(step // 2)))
    return rec()[::-1]

print(to_binary(131445))