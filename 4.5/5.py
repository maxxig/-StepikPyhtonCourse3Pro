from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as file:
    data = file.infolist()


# data.sort()
new_data = {

        d.filename.split('/')[-1]:
            {
                'date': datetime(*d.date_time).strftime('%Y-%m-%d %H:%M:%S')
                ,'orig_size': d.file_size
                ,'compress_size': d.compress_size
            }

    for d in data if d.is_dir() == False}

new_data =  {k: v for k, v in sorted(list(new_data.items()), key=lambda x:x[0])}

for key, value in new_data.items():
    print(key)
    print(f"  Дата модификации файла: {value['date']}")
    print(f"  Объем исходного файла: {value['orig_size']} байт(а)")
    print(f"  Объем сжатого файла: {value['compress_size']} байт(а)\n")