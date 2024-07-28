import sys; input = sys.stdin.readline
from heapq import heappop, heappush

n, m = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
inf = 1e10

res = [[] for _ in range(n)]

def sol(s, e):
    if s == e:
        return 0
    dist = [inf] * n
    dist[s] = 0

    q = []
    heappush(q, (0, s))
    while q:
        cost, now = heappop(q)
        if dist[now] < cost:
            continue
        for next in range(n):
            tmp = cost + road[now][next]
            if tmp < dist[next]:
                dist[next] = tmp
                heappush(q, (tmp, next))
    res[s] = dist
    return dist[e]

for _ in range(m):
    s, e, t = map(int, input().split())
    if res[s - 1]:
        if res[s - 1][e - 1] <= t:print('Enjoy other party')
        else:print('Stay here')
    else:
        if sol(s - 1, e - 1) <= t:print('Enjoy other party')
        else:print('Stay here')