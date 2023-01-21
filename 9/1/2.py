def convert(number):
    return (
        bin(number)[2:] if bin(number)[0] != '-' else ('-'+bin(number)[3:])
        ,oct(number)[2:] if oct(number)[0] != '-' else ('-'+oct(number)[3:])
        , hex(number)[2:].upper() if hex(number)[0] != '-' else ('-' + hex(number)[3:]).upper())

print(convert(-132))