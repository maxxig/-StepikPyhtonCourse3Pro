n = int(input())
my_dict = dict()
res = set()
for i in range(n):
    if i == 0:
        res = set(input().split(', '))
    else:
        res = res & set(input().split(', '))
if len(res) == 0:
    print('Сериал снять не удастся')
else:
    print(*sorted(res), sep=', ')

