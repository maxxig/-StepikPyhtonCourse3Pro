n = int(input())
book = {}
book2 = set()
def get_email_login (value):
    number_index = 0
    for i,v in enumerate(value):
        if v.isdigit():
            number_index = i
            break
    if number_index == 0:
        return  value
    else:
        return value[:number_index]

for _ in range(n):
    email = input().split('@')
    login = email[0]
    book2.add(login)

m = int(input())
for _ in range(m):
    new_user = input()
    for i in range(len(book2)+m):
        if i == 0:
            if new_user not in book2:
                print(f'{new_user}@beegeek.bzz')
                book2.add(new_user)
                break
        else:
            if (new_user+str(i)) not in book2:
                print(f'{new_user+str(i)}@beegeek.bzz')
                book2.add((new_user+str(i)))
                break