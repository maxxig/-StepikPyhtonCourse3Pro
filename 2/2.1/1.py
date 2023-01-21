def hide_card(card):
    return ''.join(list(map(lambda v: '*' if v[0] <12 else v[1], enumerate([c for c in card.replace(' ','')]))))

card = '3456 9012 5678 1234'

print(hide_card(card))