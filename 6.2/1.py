str1, str2 = input(), input()

d = {chr(97+i): item for i, item in enumerate(str1)}

tbl = str1.maketrans(d)
print(str2.lower().translate(tbl))


