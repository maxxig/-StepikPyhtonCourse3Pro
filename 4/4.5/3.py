from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    data = file.infolist()
filename, coef = '', 100

for d in data:
    if not d.is_dir():
        coef_temp = (d.compress_size/d.file_size)*100
        if coef_temp < coef:
            filename = d.filename.split('/')[-1]
            coef = coef_temp

print(filename)