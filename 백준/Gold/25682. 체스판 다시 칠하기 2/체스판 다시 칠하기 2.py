import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [[1 if i == 'W' else -1 for i in list(input())] for _ in range(n)]

chess1 = [[[1, -1][(i + j)%2] for j in range(m)] for i in range(n)]
chess2 = [[[-1, 1][(i + j)%2] for j in range(m)] for i in range(n)]

res1 = [[0] * (m + 1) for _ in range(n + 1)]
res2 = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        res1[i+1][j+1] = res1[i][j + 1] + res1[i + 1][j] - res1[i][j] + (board[i][j] != chess1[i][j])
        res2[i+1][j+1] = res2[i][j + 1] + res2[i + 1][j] - res2[i][j] + (board[i][j] != chess2[i][j])

ans = 4000000
for i in range(k, n + 1):
    for j in range(k, m + 1):
        ans = min(
            ans,
            res1[i][j] - res1[i-k][j] - res1[i][j-k] + res1[i-k][j-k],
            res2[i][j] - res2[i-k][j] - res2[i][j-k] + res2[i-k][j-k]
        )

print(ans)