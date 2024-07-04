from collections import deque as dq

r1, c1 = map(int, input().split())  # 상
r2, c2 = map(int, input().split())  # 왕
game_map = [[0] * 9 for _ in range(10)]

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상
direction2 = [(-1, 1), (1, 1), (1, -1), (-1, -1)] # idx, idx + 1
q = dq([(r1, c1, 0)])
visited = [[0] * 9 for _ in range(10)]
ans = -1

while q:
    x, y, cnt = q.popleft()
    visited[x][y] = 1
    
    if (x, y) == (r2, c2):
        ans = cnt
        break
        
    for idx in range(4):
        nx1, ny1 = x + direction[idx][0], y + direction[idx][1]
        if abs(nx1 - r2) or abs(ny1 - c2):
            for p_idx in [idx, (idx + 1) % 4]:
                nx2, ny2 = nx1 + direction2[p_idx][0], ny1 + direction2[p_idx][1]
                if abs(nx2 - r2) or abs(ny2 - c2):
                    nx, ny = nx2 + direction2[p_idx][0], ny2 + direction2[p_idx][1]
                    if nx in range(10) and ny in range(9) and not visited[nx][ny]:
                        q.append((nx, ny, cnt + 1))
print(ans)