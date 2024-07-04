import sys
from collections import deque as dq
n = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

q = dq([1])
visit = [0] * (n + 1)
while q:
    now = q.popleft()
    for i in arr[now]:
        if not visit[i]:
            visit[i] = now
            q.append(i)

print(*visit[2:], sep = '\n')
