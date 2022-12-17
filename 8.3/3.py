def number_of_frogs(years):
    if years == 1:
        return 77
    else:
        return 3*(number_of_frogs(years-1) - 30)


print(number_of_frogs(5))