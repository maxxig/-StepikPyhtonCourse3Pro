class CardDeck:
    def __init__(self):
        self.it = iter([f"{i} {j}" for j in ("пик", "треф", "бубен", "червей") for i in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.it)

cards = list(CardDeck())

try:
    next(cards)
except:
    print('Error')