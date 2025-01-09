import sys;input = sys.stdin.readline
sys.setrecursionlimit(100000)
m, n = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def sol(x=0, y=0):
    if (x, y) == (m - 1, n - 1):return 1
    if dp[x][y] != -1:return dp[x][y]
    dp[x][y] = 0
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if nx in range(m) and ny in range(n):
            if heights[nx][ny] < heights[x][y]:
                dp[x][y] += sol(nx, ny)

    return dp[x][y]

print(sol())