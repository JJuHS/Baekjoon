import sys
input = sys.stdin.readline
from heapq import heappush, heappop
q1, q2 = [], []

for _ in range(int(input())):
    n = int(input())

    if len(q1) == len(q2):
        heappush(q1, -n)
    else:
        heappush(q2, n)

    if q1 and q2 and q1[0] + q2[0] < 0:
        n1, n2 = heappop(q1), heappop(q2)
        heappush(q1,- n2), heappush(q2, -n1)
    print(-q1[0])