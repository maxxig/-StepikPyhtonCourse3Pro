from itertools import product

src = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
n, m = int(input()), int(input())

sys_num_arr = src[:n]

combin = product(sys_num_arr, repeat=m)

print(*[''.join(c) for c in combin])