from collections import ChainMap

def get_all_values (cm, n):
    arr = [c.get(n) for c in cm.maps if c.get((n)) != None]
    if len(arr) > 0:
        return set(arr)
    else:
        return set()


chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'city': 'Almetyevsk'}, {'name': 'Timur', 'age': 29, 'city': 'Moscow'})
result = get_all_values(chainmap, 'city')

print(*sorted(result))