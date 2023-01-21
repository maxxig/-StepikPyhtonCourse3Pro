from datetime import datetime, timedelta

current_date = datetime.strptime(input(),'%d.%m.%Y')
tmp_date = (current_date + timedelta(days=1))
ddays = set()
while (tmp_date <= (current_date + timedelta(days=7))):
    ddays.add(tmp_date)
    tmp_date = (tmp_date + timedelta(days=1))

staff = dict()
for _ in range(int(input())):
    full_unput = input().split()
    name = f'{full_unput[0]} {full_unput[1]}'
    dr = datetime.strptime(full_unput[2],'%d.%m.%Y')
    for s in ddays:
        if dr.replace(year=s.year) == s:
            staff[dr] = name

print(staff.get(max(staff, default=None), 'Дни рождения не планируются'))
