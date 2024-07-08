from heapq import heappop, heappush
import sys; input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]   # 무게, 가격
jewels.sort()
bags = [int(input()) for _ in range(k)]
bags.sort()
res = 0
tmp = []

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heappush(tmp, -heappop(jewels)[1])
    if tmp:
        res -= heappop(tmp)

print(res)