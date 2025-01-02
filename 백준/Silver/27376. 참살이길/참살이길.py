import sys;input = sys.stdin.readline

from heapq import heappop, heappush

n, k = map(int, input().split())
arr = []
for _ in range(k):
    x, t, s = list(map(int, input().split()))
    heappush(arr, (x, t, s))

time = 0
now = 0
for _ in range(k):
    x, t, s = heappop(arr)
    if now < x:
        time += x - now
        now = x
    if (time - s) % (2 * t) < t:
        continue
    else:
        time += 2 * t - ((time - s) % (2 * t))

print(time + n - now)

    