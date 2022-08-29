with open('files.txt', encoding='utf-8') as f:
    data = f.readlines()

def convert_to_bytes (number, uom):
    if uom == 'B':
        return number
    elif uom == 'KB':
        return number * 1024
    elif uom == 'MB':
        return number * 1024 * 1024
    elif uom == 'GB':
        return number * 1024 * 1024 * 1024
def convert_butes_to (number):
    if number < 1024:
        return str(number) + ' B'
    elif number < 1024 * 1024:
        return str(round(number/1024)) + ' KB'
    elif number < 1024 * 1024 * 1024:
        return str(round(number/(1024 * 1024))) + ' MB'
    elif number < 1024 * 1024 * 1024 * 1024:
        return str(round(number/(1024 * 1024 * 1024))) + ' GB'
def my_print(grouped_files_for_print_l):
    for p in grouped_files_for_print_l:
        print(p)
    print('----------')
    print(f'Summary: {convert_butes_to(sum_size)}')
    print()
all_files_dict = {}
for d in data:
    d_item = d.split()
    ext_item = d_item[0].split('.')
    values = dict(ext = ext_item[1], size = convert_to_bytes(int(d_item[1]), d_item[2].rstrip()))
    all_files_dict[d_item[0]] = values
# print(data)
# print(all_files_dict)
last_ext, sum_size, grouped_files_for_print = '', 0, []
for k, m_d in sorted(all_files_dict.items(), key=lambda x: (x[1]['ext'], x[0])):
    # print(k, m_d)
    if m_d.get('ext') != last_ext and last_ext !='':
        my_print(grouped_files_for_print)
        sum_size = 0
        grouped_files_for_print.clear()
    last_ext = m_d.get('ext')
    sum_size += m_d.get('size')
    grouped_files_for_print.append(k)
my_print(grouped_files_for_print)

