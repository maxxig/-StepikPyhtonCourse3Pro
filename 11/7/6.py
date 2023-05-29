import re
def abbreviate(phrase):
    res = re.findall(r'[A-Z]{0,1}[a-z]{1,}|[A-Z]{1}', phrase)
    res2 = list(map(lambda x: x[0].upper(), res))
    return ''.join(res2)

print(abbreviate('JavaScript object Notation'))
print(abbreviate('JS game sec'))