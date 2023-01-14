def generator_square_polynom(a, b, c):
    def func(x):
        return a * x * x + b * x + c
    return func


print(generator_square_polynom(0, 0, 0)(126484.38483))