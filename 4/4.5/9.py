from zipfile import ZipFile
import json

res = []
with ZipFile('data.zip') as file:
    data = file.infolist()
    for d in data:
        if d.is_dir() == False and d.filename.split('.')[-1] == 'json':
            file.extract(d.filename)
            with open(d.filename, encoding='utf-8') as input_file:
                try:
                    json_data = json.load(input_file)
                except:
                    pass
            if json_data['team'] == 'Arsenal':
                res.append(f"{json_data['first_name']} {json_data['last_name']}")
res = sorted(res, key= lambda x: (x.split()[0], x.split()[1]))
print(*res, sep = '\n')