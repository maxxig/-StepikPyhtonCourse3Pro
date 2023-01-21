class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if (len(string) < 9):
        raise LengthError
    elif not any(s.islower() for s in string) or not any(s.isupper() for s in string):
        raise LetterError
    elif not any(s.isdigit() for s in string):
        raise DigitError
    return True


try:
    print(is_good_password('123456789A'))
except Exception as err:
    print(type(err))