import math
from heapq import heappop, heappush
n, w = map(int, input().split())
m = float(input())

location = [0]           # i 번 발전소의 좌표
for _ in range(n):
    x, y = map(int, input().split())
    location.append((x, y))

inf = 1e10
dp = [inf] * (n + 1)
dp[1] = 0
dic = {}
for i in range(w):
    x, y = map(int, input().split())

    if x in dic: dic[x].append(y)
    else: dic[x] = [y]

    if y in dic: dic[y].append(x)
    else: dic[y] = [x]

q = []
heappush(q, (0, 1))     # distance, index
while q:
    dist, now = heappop(q)
    tmp_arr = []
    if now in dic:
        tmp_arr = dic[now]
    if dp[now] < dist:
        continue
    x, y = location[now]
    for next in range(1, n + 1):
        if next == now:
            continue
        if next in tmp_arr:
            if dp[next] > dist:
                dp[next] = dist
                heappush(q, (dist, next))
                continue
        nx, ny = location[next]
        euclidean_dist = math.dist((x, y), (nx, ny))
        if euclidean_dist > m: continue
        if dp[next] <= euclidean_dist + dist: continue
        dp[next] = euclidean_dist + dist
        heappush(q, (euclidean_dist + dist, next))

res = int(dp[-1] * 1000)
print(res)