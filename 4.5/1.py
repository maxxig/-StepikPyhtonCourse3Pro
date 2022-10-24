from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    data = file.infolist()
count = 0
for d in data:
    if not d.is_dir():
    # if d.filename[-1] !='/':
        count += 1
print(count)