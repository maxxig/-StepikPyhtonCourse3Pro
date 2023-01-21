from collections import Counter
word = 's'
words = 'sdsf sds sdfsdg S dhgf gfd asd'


def count_occurences(word, words):
    cn = Counter(list(map(lambda x: x.lower(),words.split())))
    return cn[word.lower()]

print(count_occurences(word, words))