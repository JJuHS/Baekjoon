from heapq import heappop, heappush
import sys;input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
inf = 1e10

order = [[] for _ in range(k + 1)]
q = []

now, next = [0] * (k + 1), [0] * (k + 1)

for i in range(k):
    order[arr[i]].append(i)

cnt, res = 0, 0

for i in range(k):
    idx = arr[i]

    if cnt == n and not now[idx]:
        p, v = heappop(q)
        now[v] = 0
        res += 1
        cnt -= 1

    next_idx = 0
    if next[idx] == len(order[idx]) - 1:
        next_idx = inf
    else:
        next[idx] += 1
        next_idx = order[idx][next[idx]]

    if not now[idx]:
        cnt += 1
        now[idx] = 1

    heappush(q, (-next_idx, idx))

print(res)