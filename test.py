from collections import OrderedDict

physicists = OrderedDict(newton='1642-1726', einstein='1879-1955')
biologists = OrderedDict(darwin='1809-1882', mendel='1822-1884',newton='1642-1727')

print(physicists | biologists)
