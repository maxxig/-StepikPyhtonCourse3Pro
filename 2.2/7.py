str_vov = 'а, у, о, ы, и, э, я, ю, ё, е'.replace(', ', '')
str_cons = 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ, ь'.replace(', ', '')
def cut_to_last_vowel(value):
    max_index = 0
    for i,v in enumerate(value):
        if v in str_vov:
            max_index= i
    return value[:max_index+1]

master = input()

m = list(map(lambda x:1 if x in str_vov else 0, cut_to_last_vowel(master)))
n = int(input())
for _ in range(n):
    check_word = input()
    c = list(map(lambda x:1 if x in str_vov else 0, cut_to_last_vowel(check_word)))
    need_print = 1
    for y in range(len(m)):
        if len(c) < len(m):
            need_print = 0
            break
        if c[y] == m[y]:
            continue
        else:
            need_print = 0
            break
    if need_print == 1:
        print(check_word)