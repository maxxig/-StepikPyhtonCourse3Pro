import re
s = input()
if re.match(r'^((Здравствуйте)|(Доброе утро)|(Добрый день)|(Добрый вечер))', s, flags=re.IGNORECASE):
    print('True')
else:
    print('False')