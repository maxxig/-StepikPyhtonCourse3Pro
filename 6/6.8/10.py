from collections import Counter

books = Counter(input().split())

total = 0
for i in range(int(input())):
    customer = input().split()
    if customer[0] in books and books.get(customer[0]) > 0:
        total += int(customer[1])
        books[customer[0]] -= 1

print(total)

