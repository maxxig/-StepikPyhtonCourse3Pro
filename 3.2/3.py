from datetime import date
n = int(input())
dates = [date.fromisoformat(input()) for _ in range(n)]
dates.sort()
print(*list(map(lambda x: x.strftime('%d/%m/%Y'), dates)), sep = '\n')