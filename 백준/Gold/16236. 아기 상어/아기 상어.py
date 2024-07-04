import sys
from collections import deque as dq
imput = sys.stdin.readline
n = int(input())
sea = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 9:
            start = (i, j)
    sea.append(tmp)


direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def bfs(s, size):
    visited = [[0] * n for _ in range(n)]
    visited[s[0]][s[1]] = 1
    time = [[0] * n for _ in range(n)]
    q = dq([s])
    tmp = []

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + direction[i][0]
            ny = now_y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if sea[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    time[nx][ny] = time[now_x][now_y] + 1
                    if 0 < sea[nx][ny] < size:
                        tmp.append([nx, ny, time[nx][ny]])
    return sorted(tmp, key = lambda x: (-x[2], -x[0], -x[1]))

res = 0
large = 2
cnt = 0
sea[start[0]][start[1]] = 0

while True:
    shark = bfs(start, large)
    if not shark:
        break
    x, y, time_ = shark.pop()
    sea[x][y] = 0
    res += time_
    cnt += 1
    start = (x, y)
    if cnt == large:
        cnt = 0
        large += 1
print(res)
