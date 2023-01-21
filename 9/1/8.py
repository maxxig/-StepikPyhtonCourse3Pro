def my_pow(number):
    res = 0
    for i, n in enumerate(str(number), 1):
        res += pow(int(n),i)
    return res


print(my_pow(1526270350334812228722339330891))