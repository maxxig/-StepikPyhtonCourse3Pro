def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    res = 0
    res = sum(filter(lambda x: True if type(x) in (int, float) else False, elems))
    return res

print(numbers_sum([10, 100, 1000, 10000]))