def filter_names(names, ignore_char, max_names):
    i = 0
    for name in names:
        if i>= max_names:
            return
        if not any(map(lambda x: x.isdigit(), name)) and name[0].lower() != ignore_char.lower():
            i += 1
            yield name

# INPUT DATA:

# TEST_1:
data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))

# TEST_2:
data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))

# TEST_3:
data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']

print(*filter_names(data, 'A', 100))

# TEST_4:
data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']

print(*filter_names(data, 'F', 6))

# TEST_5:
data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']

print(*filter_names(data, 'A', 22))

# TEST_6:
data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']

print(next(filter_names(data, 'R', 1)))

# TEST_7:
data = ['Barry']

print(*filter_names(data, 'B', 1))

# TEST_8:
data = ['Dima1', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', '4Ruslan']

print(*filter_names(data, 'a', 20))

# TEST_9:
data = ['Dima', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', '4Ruslan']

print(*filter_names(data, 'A', 1))

# TEST_10:
data = ['1Dima', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', 'Ruslan']

print(*filter_names(data, 'A', 1))

# TEST_11:
data = []

print(list(filter_names(data, 'B', 1)))

# TEST_12:
data = ['Dima', 'Timur', 'Arthur', 'Anri', 'Arina', 'German', 'Ruslan', 'Roma5', 'Jenya', 'Anna']

print(*filter_names(data, 'A', 8))
