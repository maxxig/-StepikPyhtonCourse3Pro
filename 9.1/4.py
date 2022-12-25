def non_negative_even(numbers):
    return all(map(lambda x: True if x>=0 and x % 2 == 0 else False, numbers))

print(non_negative_even([64, 78, 4454, 234, 90, 78, 0, 67676]))