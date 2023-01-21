def extract_this(zip_name, *args):
    from zipfile import ZipFile
    with ZipFile(zip_name) as file:
        data = file.infolist()
        if len(args) == 0:
            file.extractall()
        else:
            for d in data:
                if d.filename.split('/')[-1] in args:
                    file.extract(d.filename)



extract_this('workbook.zip', 'earth.jpg', 'exam.txt')