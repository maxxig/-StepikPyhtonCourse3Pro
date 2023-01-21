def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    index_nearest, res_index = abs(number - numbers[0]), 0
    for i, n in enumerate(numbers):
        if abs(number - n) < index_nearest:
            index_nearest = abs(number - n)
            res_index = i
    return res_index


print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))