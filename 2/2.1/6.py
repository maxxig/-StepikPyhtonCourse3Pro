def create_anagram_dict (w):
    d = {}
    for w in w:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d
def filter_anagrams(word, words):
    word_dict = create_anagram_dict(word)
    return list(filter(lambda x: create_anagram_dict(x) == word_dict, words))


word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

# print(filter_anagrams(word, anagrams))
# print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
# print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('стекло', []))