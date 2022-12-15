try:
    with open(input(),'r', encoding='utf-8') as file:
        data = file.readlines()
    print(*[d.rstrip() for d in data], sep='\n')
except:
    print("Файл не найден")
