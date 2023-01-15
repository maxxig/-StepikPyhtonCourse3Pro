f = input()
values = input().split(' ')
frm = int(values[0])
to = int(values[1])
min_value, max_value = None, None
for x in range(frm, to+1):
    result = eval(f)
    if min_value is None or result < min_value :
        min_value = result
    if max_value is None or result > max_value:
        max_value = result

print(f"Минимальное значение функции {f} на отрезке [{frm}; {to}] равно {min_value}")
print(f"Максимальное значение функции {f} на отрезке [{frm}; {to}] равно {max_value}")
