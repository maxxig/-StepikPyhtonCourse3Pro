from datetime import date, datetime

with open('diary.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
info = dict()
message_text = ''
dt1 = date(1977,1,1)
is_end_message = False
for d in data:
    if d =='\n':
        is_end_message = True
    if is_end_message == True:
        info[dt1] = message_text
        is_end_message = False
        message_text = ''
    else:
        try:
            dt1 = datetime.strptime(d.rstrip(),'%d.%m.%Y; %H:%M')
        except:
            message_text += d
info[dt1] = message_text + '\n'

for k,i in sorted(info.items()):
    print(k.strftime('%d.%m.%Y; %H:%M'), i, sep='\n')