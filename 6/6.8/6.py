from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.max_values = lambda: [(k, v) for k, v in data.items() if v == data.most_common()[0][1]]
data.min_values = lambda: [(k, v) for k, v in data.items() if v == data.most_common()[-1][1]]

print(data.max_values())
print(data.min_values())