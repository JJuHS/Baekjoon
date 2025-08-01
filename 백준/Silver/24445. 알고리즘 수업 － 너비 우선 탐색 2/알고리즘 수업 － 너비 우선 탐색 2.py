import sys; input = sys.stdin.readline
from collections import deque as dq

n, m, r = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    
res = [0] * (n + 1)
visit = [0] * (n + 1)

visit[r] = 1
q = dq([r])
cnt = 1
res[r] = cnt

while q:
    now = q.popleft()
    arr[now].sort(reverse=True)
    
    for a in arr[now]:
        if not visit[a]:
            visit[a] = 1
            cnt += 1
            res[a] = cnt
            q.append(a)
                
for i in range(n):
    print(res[i+1])
