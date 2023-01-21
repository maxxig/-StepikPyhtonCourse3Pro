def is_greater(lists, number):
    return any(map(lambda x: True if sum(x) > number else False, lists))


data = [[1, 5, 22, -9], [6, 9, 0, -1, -1], [1, 1, 1], [4, 5, 6, 7], [5, 0, 0, -10, -10]]

print(is_greater(data, 1))