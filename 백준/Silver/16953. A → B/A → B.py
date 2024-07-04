from heapq import heappop, heappush
a, b = map(int, input().split())
q = []
heappush(q, (a, 1))

while q:
    num, cnt = heappop(q)
    if num == b:
        print(cnt)
        exit(0)
    if num > b:
        print(-1)
        exit(0)
    heappush(q, (num * 2, cnt + 1))
    heappush(q, (num * 10 + 1, cnt + 1))
