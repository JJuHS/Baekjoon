import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
m, n = map(int, input().split())
tomato = []
visited = [[False] * m for _ in range(n)]
start = []
cnt = 0
for i in range(n):
    tmp_list = list(map(int, input().split()))
    tomato.append(tmp_list)
    for j in range(m):
        if tmp_list[j] == -1:
            visited[i][j] = True
            cnt += 1
        if tmp_list[j] == 1:
            start.append((i, j))
            visited[i][j] = True
            cnt += 1

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(tomato_map, start_):
    global cnt
    day = 0
    q = start_
    while q:
        tmp_q = []
        for tom in q:
            for k in range(4):
                tmp_x = tom[0] + direction[k][0]
                tmp_y = tom[1] + direction[k][1]
                if 0 <= tmp_x < n and 0 <= tmp_y < m and not visited[tmp_x][tmp_y]:
                    tmp_q.append((tmp_x, tmp_y))
                    visited[tmp_x][tmp_y] = True
                    cnt += 1
        q = tmp_q
        day += 1
    return day

res = bfs(tomato, start)
print([res-1, -1][1- (cnt == n*m)])