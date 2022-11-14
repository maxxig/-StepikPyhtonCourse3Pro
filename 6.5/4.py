from collections import defaultdict

def wins(pairs):
    def_dict = defaultdict(set)
    for pr in pairs:
        def_dict[pr[0]].add(pr[1])
    return def_dict


result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))