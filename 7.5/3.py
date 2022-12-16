import sys
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
        raise LengthError('LengthError')
    elif not any(s.islower() for s in string) or not any(s.isupper() for s in string):
        raise LetterError('LetterError')
    elif not any(s.isdigit() for s in string):
        raise DigitError('DigitError')
    return True

for p in [s.strip() for s in sys.stdin]:
    try:
        is_good_password(p)
        print('Success!')
        break
    except Exception as e:
        print(e)

