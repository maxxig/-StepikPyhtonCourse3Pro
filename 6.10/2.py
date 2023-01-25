from collections import ChainMap

def deep_update (cm, k, v):
    if k in cm:
        for c in cm.maps:
            if k in c:
                c[k] = v
    else:
        cm[k] = v

chainmap = ChainMap({'name': 'Tanya'}, {'name': 'Arthur'}, {'name': 'Timur'})

deep_update(chainmap, 'name', 'Dima')

print(chainmap)