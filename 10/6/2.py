def is_prime(number):
    if number > 1 and all(bool(number % n) for n in range(2, number)):
        return True
    else:
        return False
    # res = (bool(number % n) for n in range(2, number))
    # print(*res)


# INPUT DATA:

# TEST_1:
print(is_prime(7))

# TEST_2:
print(is_prime(8))

# TEST_3:
print(is_prime(1))

# TEST_4:
print(is_prime(16))

# TEST_5:
print(is_prime(27))

# TEST_6:
print(is_prime(13))

# TEST_7:
print(is_prime(421))

# TEST_8:
print(is_prime(1061))

# TEST_9:
print(is_prime(9973))
