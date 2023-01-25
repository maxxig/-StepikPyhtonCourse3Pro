from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

cm = ChainMap(bread, meat, sauce, vegetables, toppings)

cn = Counter(input().split(','))

max_len = len(max(cn.keys(), key=lambda x: len(x)))
total = 0
max_str_len = 0
for k, v in sorted(cn.items(), key=lambda x: x[0]):
    print_str = f"{k.ljust(max_len,' ')} x {v}"
    print(print_str)
    if len(print_str) > max_str_len:
        max_str_len = len(print_str)
    total += v * cm[k]
result_text = f"ИТОГ: {total}р"
if len(result_text) > max_str_len:
    max_str_len = len(result_text)
print('-'.ljust(max_str_len,'-'))
print(result_text)
