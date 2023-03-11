def nonempty_lines(file):
    with open (file, 'r', encoding='UTF-8') as file:
        file_lines = (line.rstrip() for line in file)
        wo_empty = (line for line in file_lines if len(line) > 0)
        for i in wo_empty:
            if len(i) > 25:
                yield '...'
            else:
                yield i


#
# # TEST_5:
print(*nonempty_lines('file5.txt'))
