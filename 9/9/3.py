from functools import  lru_cache
@lru_cache()
def ways(n):
    if n <= 0:
        return 0
    elif n == 1:
        return  1
    else:
        return ways(n-1) + ways(n-3) + ways(n-4)

print(ways(100))