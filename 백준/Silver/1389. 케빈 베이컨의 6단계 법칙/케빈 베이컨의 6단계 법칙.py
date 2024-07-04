from collections import deque as dq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
user = [[0] * (n + 1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    user[a][b] = 1
    user[b][a] = 1

q = dq()
def bfs(arr, i):
    num = [0] * (n + 1)
    visited = [i]
    q = dq([i])
    while q:
        s = q.popleft()
        for j in range(n + 1):
            if arr[s][j] and j not in visited:
                q.append(j)
                visited.append(j)
                num[j] = num[s] + 1
    return sum(num)

res = []
for i in range(1, n + 1):
    result = bfs(user, i)
    res.append(result)
a = res.index(min(res)) + 1
print(a)

