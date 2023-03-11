def card_deck(suit):
    cards = ["пик", "треф", "бубен", "червей"]
    cards.remove(suit)
    while(1):
        yield from iter([f"{i} {j}" for j in cards for i in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")])


generator = card_deck('пик')

cards = [next(generator) for _ in range(80)]

print(*cards)
