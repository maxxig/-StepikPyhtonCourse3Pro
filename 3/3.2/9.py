from datetime import date
def is_correct(d, m, y):
    try:
        date(y, m, d)
        return True
    except:
        return False

my_arr = []
cnt = 0
while(True):
    s  = input()
    if s == 'end':
        break
    else:
        _s = s.split('.')
        if is_correct(int(_s[0]),int(_s[1]),int(_s[2])):
            print('Корректная')
            cnt +=1
        else:
            print('Некорректная')
print(cnt)