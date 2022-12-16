import json
try:
    with open(input(),'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            print(data)
        except:
            print('Ошибка при десериализации')
except FileNotFoundError:
    print("Файл не найден")
