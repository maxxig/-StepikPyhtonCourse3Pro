from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    data = file.infolist()

size, compress_size = 0, 0
for d in data:
    if not d.is_dir():
        size += d.file_size
        compress_size += d.compress_size
print(f'Объем исходных файлов: {size} байт(а)')
print(f'Объем сжатых файлов: {compress_size} байт(а)')
