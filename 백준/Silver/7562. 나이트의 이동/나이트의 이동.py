import sys; input = sys.stdin.readline
from collections import deque as dq

def sol(a, b, x, y):
    q = dq([(a, b)])
    visit = [[0] * l for _ in range(l)]
    visit[a][b] = 1
    
    while q:
        now1, now2 = q.popleft()
        cnt = visit[now1][now2]
        
        for dx, dy in [(2,1),(1,2),(-2,1),(-1,2),(1,-2),(2,-1),(-1,-2),(-2,-1)]:
            nx, ny = now1 + dx, now2 + dy
            if nx in range(l) and ny in range(l) and not visit[nx][ny]:
                if (nx, ny) == (x, y):
                    print(cnt)
                    return
                visit[nx][ny] = cnt + 1
                q.append((nx, ny))
                
for _ in range(int(input())):
    l = int(input())
    X, Y = map(int, input().split())
    A, B = map(int, input().split())
    
    if (X == A) and (Y == B):
        print(0)
        continue
        
    sol(A, B, X, Y)

                
    
    
    