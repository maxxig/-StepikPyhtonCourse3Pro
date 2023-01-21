from datetime import date
def is_correct(d, m, y):
    try:
        date(y, m, d)
        return True
    except:
        return False

print(is_correct(31, 12, 2021))
print(is_correct(31, 13, 2021))