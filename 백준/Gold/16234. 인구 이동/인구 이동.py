from collections import deque as dq
import sys; input = sys.stdin.readline
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
border = [[0] * n for _ in range(n)]


def bfs(a, b):
    q = dq([(a, b)])
    tmp = [(a, b)]
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx in range(n) and ny in range(n) and not visit[nx][ny]:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    visit[nx][ny] = 1
                    q.append((nx, ny))
                    tmp.append((nx, ny))
    return tmp


res = 0
while 1:
    visit = [[0] * n for _ in range(n)]
    cycle = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = 1
                union = bfs(i, j)
                if len(union) > 1:
                    cycle = 1
                    average = sum(arr[x][y] for x, y in union) // len(union)
                    for a, b in union:
                        arr[a][b] = average
    if not cycle:
        print(res)
        break
    res += 1
