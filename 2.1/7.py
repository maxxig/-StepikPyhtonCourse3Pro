def likes(names):
    if len(names) == 0:
        return 'Никто не оценил данную запись'
    if len(names) == 1:
        return f'{names[0]} оценил(а) данную запись'
    if len(names) == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else:
        return f'{names[0]}, {names[1]} и {len(names)-2} других оценили данную запись'

print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))
print(likes(['Эндрю', 'Тоби', 'Том']))