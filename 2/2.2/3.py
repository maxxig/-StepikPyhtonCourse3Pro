inp = input().split()
n = int(inp[0])
x = int(inp[1])
y = int(inp[2])
a = int(inp[3])
b = int(inp[4])
arr = [g for g in range(1, n+1)]
p1 = arr[x-1:y]
p1.reverse()
arr[x-1:y] = p1
p2 = arr[a-1:b]
p2.reverse()
arr[a-1:b] = p2
print(*arr)