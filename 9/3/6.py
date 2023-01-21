#print(chr(91))

def verification(login, password, success, failure):
    a,b,c,d, text = False,False,False,False, ''
    for p in password:
        if p.isalpha() and ord(p)>=65 and ord(p)<=122 and not a:
            a = True
        if p.isdigit() and not d:
            d = True
        if p.islower() and ord(p)>=97 and ord(p)<=122 and not b:
            b = True
        if p.isupper() and ord(p)>=65 and ord(p)<=90 and not c:
            c = True
    if all([a, b, c, d]):
        success(login)
    else:
        if a == False:
            text = 'в пароле нет ни одной буквы'
        elif c == False:
            text = 'в пароле нет ни одной заглавной буквы'
        elif b == False:
            text = 'в пароле нет ни одной строчной буквы'
        else:
            text = 'в пароле нет ни одной цифры'
        failure(login, text)
    #print(a,b,c,d)


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'qwerty', success, failure)