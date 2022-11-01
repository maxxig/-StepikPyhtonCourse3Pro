from zipfile import ZipFile

def convert_butes_to (number):
    if number < 1024:
        return str(number) + ' B'
    elif number < 1024 * 1024:
        return str(round(number/1024)) + ' KB'
    elif number < 1024 * 1024 * 1024:
        return str(round(number/(1024 * 1024))) + ' MB'
    elif number < 1024 * 1024 * 1024 * 1024:
        return str(round(number/(1024 * 1024 * 1024))) + ' GB'

with ZipFile('desktop.zip') as file:
    data = file.infolist()
    for d in data:
        current = d.filename.rstrip('/').split('/')
        result = "  " * (len(current)-1)
        result += current[-1]
        if not d.is_dir():
            result += ' ' + convert_butes_to(d.file_size)
        print(result)