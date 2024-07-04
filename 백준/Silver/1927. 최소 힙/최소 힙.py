import sys
import heapq

n = int(input())

x = []

for _ in range(n):
    y = int(sys.stdin.readline())

    if y == 0:
        if x:
            print(heapq.heappop(x))
        else:
            print(0)
    else:
        heapq.heappush(x, y)