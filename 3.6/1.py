import time
def add(a, b, c):
    time.sleep(5)
    return a + b + c

def calculate_it(f, *args):
    start_time = time.perf_counter()
    res = f(*args)
    end_time = time.perf_counter()
    t = end_time - start_time
    return (res, t)

print(calculate_it(add, 1, 2, 3))