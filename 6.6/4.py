from collections import OrderedDict
data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)


def custom_sort(data, by_values=False):
    if by_values:
        for k, v in sorted(data.items(), key=lambda x:x[1]):
            data.move_to_end(k)
    else:
        for d in sorted(data.keys()):
            data.move_to_end(d)

# custom_sort(data, by_values=False)
#
# print(*data.items())

data = OrderedDict(e=11, b=22, a=99, g=66, c=44, d=33, h=99, f=77, i=88)
custom_sort(data)

print(*data.items())