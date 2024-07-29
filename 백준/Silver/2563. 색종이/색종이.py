res = [[0] * 101 for _ in range(101)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if i < 101 and j < 101:
                res[i][j] = 1
ans = 0
for r in res:ans += sum(r)
print(ans)