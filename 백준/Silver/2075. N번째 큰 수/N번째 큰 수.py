import sys; input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
arr = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for a in tmp:
        if len(arr) < n:
            heappush(arr, a)
        else:
            if arr[0] < a:
                heappop(arr)
                heappush(arr, a)
print(arr[0])