import sys
from collections import deque as dq

input = sys.stdin.readline
n, m = map(int, input().split())
maze = [[0] * m for _ in range(n)]
for i in range(n):
    tmp = input()
    for j in range(m):
        if tmp[j] == '1':
            maze[i][j] = 1

start = (0, 0)
end = (n - 1, m - 1)
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = dq()
q.append(start)
visit_cnt = [[10005] * m for _ in range(n)]
visit_cnt[0][0] = 1
while q:
    now = q.popleft()
    for i in range(4):
        tmp_x = now[0] + direction[i][0]
        tmp_y = now[1] + direction[i][1]
        if 0 <= tmp_x < n and 0 <= tmp_y < m:
            if visit_cnt[tmp_x][tmp_y] == 10005 and maze[tmp_x][tmp_y]:
                visit_cnt[tmp_x][tmp_y] = min(visit_cnt[now[0]][now[1]] + 1, visit_cnt[tmp_x][tmp_y])
                q.append((tmp_x, tmp_y))

print(visit_cnt[n - 1][m - 1])