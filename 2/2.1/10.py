def choose_plural(num, tuple):
    if int(str(num)[-1]) in [0,5,6,7,8,9]:
        return f'{num} {tuple[2]}'
    if len(str(num))>1 and int(str(num)[-2:]) in [11,12,13,14]:
        return f'{num} {tuple[2]}'
    if int(str(num)[-1]) in [2,3,4]:
        return f'{num} {tuple[1]}'
    if int(str(num)[-1]) == 1:
        return f'{num} {tuple[0]}'


print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(173, ('яблоко', 'яблока', 'яблок')))