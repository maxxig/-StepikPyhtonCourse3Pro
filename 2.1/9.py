def spell(*args):
    res = dict()
    for a in args:
        if a[0].lower() not in res:
            res[a[0].lower()] = len(a)
        else:
            if len(a)> res[a[0].lower()]:
                res[a[0].lower()] = len(a)
    return res

words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))