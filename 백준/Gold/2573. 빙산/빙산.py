from collections import deque as dq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]

def bfs(a, b):
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = dq([[a, b]])
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx , ny = x + dx, y + dy
            if nx in range(n) and ny in range(m):
                if not visited[nx][ny]:
                    if sea[nx][ny]:  # 빙산이 있는 경우 방문 표시하고 q에 넣게
                        visited[nx][ny] = True
                        q.append([nx, ny])
                    else:  # 바다인 경우 녹일 양 만들어주기
                        meet_sea[x][y] += 1
    return 1

t = 0

while 1:
    res = []  # 빙산의 덩어리 개수
    visited = [[0] * m for _ in range(n)]
    meet_sea = [[0] * m for _ in range(n)]

    # 각 빙산의 덩어리를 탐색하면서 덩어리 개수 확인
    for i in range(n):
        for j in range(m):
            if sea[i][j] and not visited[i][j]:
                res.append(bfs(i, j))

    # 빙산 녹이기
    for i in range(n):
        for j in range(m):
            sea[i][j] -= meet_sea[i][j]
            if sea[i][j] < 0:
                sea[i][j] = 0

    # 빙산 덩어리가 2개 이상이거나 0개이면 반복문 종료
    if len(res) != 1:
        break
    t += 1

print(t) if len(res) >= 2 else print(0)
