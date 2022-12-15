def get_id (names, name):
    try:
        if type(name) == str:
            if not name.istitle():
                raise  ValueError
            for n in name:
                try:
                    int(n)
                except:
                    continue
                else:
                    raise ValueError
        elif type(name) != str:
            raise TypeError
    except ValueError as err:
        raise ValueError('Имя не является корректным') from err
    except TypeError as err:
        raise TypeError('Имя не является строкой') from err
    else:
        return len(names)+1

names = ['Timur', 'Anri', 'Dima', 'Roma', 'Gvido', 'Rosy', 'Soslan', 'Natasha', 'Arthur']
name = 'Arthur'

print(get_id(names, name))