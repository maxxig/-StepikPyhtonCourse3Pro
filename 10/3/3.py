def is_iterator(obj):
    return True if '__next__'in obj.__dir__() else False


beegeek = 'beegeek'

print(is_iterator(beegeek))