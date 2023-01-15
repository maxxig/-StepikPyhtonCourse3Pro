def print_operation_table(operation, rows, cols):
    mass = [[0]*cols for r in range(rows)]
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            mass[r-1][c-1] = operation(r, c)

    for r in range(rows):
        print(*mass[r])

from operator import mul
print_operation_table(mul, 5, 10)