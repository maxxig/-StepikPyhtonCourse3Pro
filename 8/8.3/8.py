def is_power(number):
    if number < 2 and number == 1.0:
        return True
    elif number < 2 and number != 1.0:
        return False
    else:
        return is_power(number/2)

print(is_power(1))