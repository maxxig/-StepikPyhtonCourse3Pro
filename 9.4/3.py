def polynom(x):
    res = x*x + 1
    polynom.values.add(res)
    return res
polynom.values = set()

for _ in range(10):
    polynom(10)

print(polynom.values)