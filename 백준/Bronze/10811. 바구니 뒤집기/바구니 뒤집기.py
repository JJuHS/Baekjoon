n, m = map(int, input().split())
arr = [i for i in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i:j+1] = arr[i:j+1][::-1]
print(*arr[1:])