import time

def get_the_fastest_func(funcs, arg):
    res = [] #every func as typle (name, ime)
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        res.append((func, end_time - start_time))
    return min(res, key= lambda x: x[1])[0]


def slow(arg):
    time.sleep(3)

def fast(arg):
    time.sleep(1)

funcs = [slow, fast]

#print(get_the_fastest_func(funcs, 0))

from math import factorial                   # функция из модуля math


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

funcs = [factorial_recurrent, factorial_classic, factorial]

#print(get_the_fastest_func(funcs, 900))


def for_and_append(s):  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension(s):  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]

funcs = [for_and_append, list_comprehension]

#print(get_the_fastest_func(funcs, 0))


def for_and_append2(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension2(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function2(iterable):  # с использованием встроенной функции list()
    return list(iterable)

funcs = [for_and_append, list_comprehension,list_function2]

print(get_the_fastest_func(funcs, range(100_000)))