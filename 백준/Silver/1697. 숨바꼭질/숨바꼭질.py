# import sys
from collections import deque as dq
N, K = map(int, input().split())

visited = [0] * 100001

def bfs(n, k):
    q = dq()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000:
                if not visited[i]:
                    visited[i] = visited[x] + 1
                    q.append(i)

bfs(N, K)