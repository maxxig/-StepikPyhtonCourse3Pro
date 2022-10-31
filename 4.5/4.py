from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as file:
    data = file.infolist()

t = [d.filename.split('/')[-1] for d in data if d.is_dir() == False and datetime(*d.date_time) > datetime(2021,11,30,14,22,00)]
t.sort()

print(*t, sep='\n')