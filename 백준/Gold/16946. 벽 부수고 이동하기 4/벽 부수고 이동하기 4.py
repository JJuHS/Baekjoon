import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline

from collections import deque as dq

n, m = map(int, input().split())

maze = [list(input()) for _ in range(n)]

direction = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

res = [[0] * m for _ in range(n)]
checked = [[-1] * m for _ in range(n)]
ans = []

def bfs(a, b, idx):
    q = dq()
    q.append((a, b))

    checked[a][b] = idx
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx in range(n) and ny in range(m):
                if maze[nx][ny] == '0' and checked[nx][ny] == -1:
                    checked[nx][ny] = idx
                    q.append((nx, ny))
                    cnt += 1
    return cnt

idx = 0
for i in range(n):
    for j in range(m):
        if maze[i][j] == '0' and checked[i][j] == -1:
            ans.append(bfs(i, j, idx))
            idx += 1

for i in range(n):
    for j in range(m):
        if maze[i][j] == '1':
            area_arr = set()
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if ni in range(n) and nj in range(m) and maze[ni][nj] == '0':
                    area_arr.add(checked[ni][nj])
                
                cnt = 1
                for area in area_arr:
                    cnt += ans[area]
                res[i][j] = cnt % 10

for arr in res:
    print(''.join(map(str, arr)))
                