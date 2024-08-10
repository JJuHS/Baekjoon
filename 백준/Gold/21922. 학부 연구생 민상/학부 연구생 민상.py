import sys;input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
a, b = 0, 0
cool = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 9:
            cool.append((i, j))

visit = [[0] * m for _ in range(n)]

for a, b in cool:
    visit[a][b] = 1

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = a + dx, b + dy
        while nx in range(n) and ny in range(m):
            visit[nx][ny] = 1
            if arr[nx][ny] == 9:
                break
            if arr[nx][ny] == 3:
                dx, dy = -dy, -dx
            elif arr[nx][ny] == 4:
                dx, dy = dy, dx
            # 막히면 그만!
            elif arr[nx][ny] == 1 and dx == 0:
                break
            elif arr[nx][ny] == 2 and dy == 0:
                break

            nx += dx
            ny += dy

print(sum(sum(i) for i in visit))