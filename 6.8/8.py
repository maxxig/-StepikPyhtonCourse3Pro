from collections import Counter

def print_bar_chart(data, mark):
    cn = Counter(data)
    max_len = len(max(cn.keys(), key=lambda x: len(x)))
    for k, v in sorted(cn.items(), key=lambda x: -x[1]):
        print(f"{k.ljust(max_len,' ')} |{mark.ljust(int(v), mark)}")

my_list = ['TTT', 'TTT', 'i', 'MMMMM',  'TTT', 'MMMMM', 'MMMMM', 'uu', 'rrrr', 'MMMMM', 'uu', 'rrrr', 'MMMMM', 'rrrr', 'rrrr']

print_bar_chart(my_list, '#')