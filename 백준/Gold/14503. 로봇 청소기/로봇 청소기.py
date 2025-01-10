import sys
input = sys.stdin.readline

n, m = map(int,input().split())
R, C, D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 0:청소해야함, 1:벽, -1:청소했음
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
res = 0
def dfs(x, y, d):
    global res
    if arr[x][y] == 0:
        arr[x][y] = -1
        res += 1

    check=False
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if nx in range(n) and ny in range(m):
            if arr[nx][ny] == 0:
                check = True
    if check:
        for i in range(1,5):
            nd = (d-i)%4
            nx, ny = x + direction[nd][0], y + direction[nd][1]
            if nx in range(n) and ny in range(m):
                if arr[nx][ny] == 0:
                    dfs(nx, ny, nd)
                    return
    else:
        nx, ny = x + direction[(d+2)%4][0], y + direction[(d+2)%4][1]
        if nx in range(n) and ny in range(m):
            if arr[nx][ny] == 1:return
            dfs(nx, ny, d)

dfs(R, C, D)
print(res)