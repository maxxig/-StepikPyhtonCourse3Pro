from collections import Counter

with open("pythonzen.txt", 'r', encoding='utf-8') as file:
    data = file.read()

new_data = ''
for d in data:
    if d.isalpha():
        new_data += d.lower()

cn = Counter(new_data)

for k, v in sorted(cn.items(), key=lambda x: x[0]):
    print(f"{k}: {v}")

