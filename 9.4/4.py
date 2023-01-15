def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1
    for m in marks:
        text = text.replace(m, '')
    return text

text = '-TTTTTTTtttttttRRRRRRrrrrrr-'
print(remove_marks(text, 't'))
print(remove_marks(text, 'r'))
print(remove_marks(text, 'T'))
print(remove_marks(text, 'R'))
print(remove_marks(text, '-'))
print(remove_marks.count)