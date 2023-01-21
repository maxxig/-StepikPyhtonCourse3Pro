from typing import Union
def get_digits(number: int | float) -> list[int]:
    return list(map(lambda x: int(x), filter(lambda x: x.isnumeric(), str(number))))

print(get_digits.__annotations__)
print(*get_digits.__annotations__.keys())
print(*get_digits.__annotations__.values())