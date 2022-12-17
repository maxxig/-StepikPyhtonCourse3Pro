def range_sum(numbers, start, end):
    def rec(numbers, step=start):
        if step == end:
            return numbers[step]
        else:
            return numbers[step] + rec(numbers, step+1)
    return rec(numbers)



print(range_sum([21, 23421, 324, 347, 25, 65, 47, 85125, 9, 123, 42, 5, 6, 765, 34, 3, 32, 13, 25365547, 22, 12], 0, 0))
