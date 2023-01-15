def sort_priority(values, group):
    t1 = list(filter(lambda x: True if x in set(values) else False, group))
    t1.sort()
    t2 = list(filter(lambda x: True if x not in set(group) else False, values))
    t2.sort()
    values[:] = t1 + t2


numbers = list(range(0, 100, 5))
sort_priority(numbers, {1, 90, 95, 25, 55, 64})

print(numbers)