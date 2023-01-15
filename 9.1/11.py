string = input()

s1 = list(filter( lambda x: x.islower(), string))
s1.sort()
s1 = ''.join(s1)
s2 = list(filter( lambda x: x.isupper(), string))
s2.sort()
s2 = ''.join(s2)
s3 = list(filter( lambda x: x.isnumeric(), string))
s3 = sorted(s3, key=lambda x: (int(x) % 2 == 0, int(x) % 2 != 0, int(x)))
s3 = ''.join(s3)

print(f"{s1}{s2}{s3}")
