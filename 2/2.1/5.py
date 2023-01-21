def convert(value):
    caps, low =0,0
    for v in value:
        if v.islower():
            low += 1
        if v.isupper():
            caps += 1
    if caps > low:
        return value.upper()
    return value.lower()
print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))