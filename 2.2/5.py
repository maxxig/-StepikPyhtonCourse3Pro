n = int(input())

arr = [i for i in range(1, n + 1)]
my_dict = dict()
for v in arr:
    sum = 0
    for a in str(v):
        sum += int(a)
    if sum not in my_dict:
        my_dict[sum] = 1
    else:
        my_dict[sum] += 1
print(max(my_dict.values()))