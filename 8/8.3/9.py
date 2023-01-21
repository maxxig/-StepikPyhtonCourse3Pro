def tribonacci(number):
    cache = {1: 1, 2: 1, 3: 1}
    def rec(number):
        result = cache.get(number)
        if result is None:
            if number <= 3:
                return 1
            else:
                result = rec(number - 1) + rec(number - 2) + rec(number - 3)
                cache[number] = result
        return result
    return rec(number)

print(tribonacci(100))