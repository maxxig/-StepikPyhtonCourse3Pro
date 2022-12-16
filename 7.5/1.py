def is_good_password(string):
    if (len(string) >= 9 and any(s.isdigit() for s in string) and any(s.islower() for s in string) and any(s.isupper() for s in string)):
        return True
    return False


print(is_good_password('qwertyтимур696969'))
