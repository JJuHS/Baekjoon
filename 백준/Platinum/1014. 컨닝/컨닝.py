def sol(x, y):
    for dx, dy in [(0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy
        if nx in range(n) and ny in range(m):
            if not visit[nx][ny] and arr[nx][ny]:
                visit[nx][ny] = 1
                if dp[nx][ny] == [-1, -1] or sol(dp[nx][ny][0], dp[nx][ny][1]):
                    dp[nx][ny] = [x, y]
                    return 1
    return 0


import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '.':
                arr[i][j] = 1
                res += 1
            else:
                arr[i][j] = 0
    dp = [[[-1, -1] for _ in range(m)] for __ in range(n)]
    for i in range(n):
        for j in range(0, m, 2):
            if arr[i][j]:
                visit = [[0] * m for _ in range(n)]
                if sol(i, j):
                    res -= 1
    print(res)