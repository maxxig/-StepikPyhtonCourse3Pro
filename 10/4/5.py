class PowerOf:
    def __init__(self, number):
        self.number = number
        self.current_paw = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_paw += 1
        return pow(self.number,self.current_paw)


power_of_two = PowerOf(100)

for _ in range(20):
    next(power_of_two)

print(next(power_of_two))