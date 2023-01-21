string = input()

res = eval(string)
if isinstance(res, list):
    print(res[-1])
elif isinstance(res, tuple):
    print(res[0])
elif isinstance(res, set):
    print(len(res))
