import sys

data = [d for d in sys.stdin]
total_numer, str_couner = 0, 0
for d in data:
    try:
        total_numer += int(d)
    except:
        try:
            total_numer += float(d)
        except:
            str_couner +=1
print(total_numer, str_couner, sep = '\n')