import sys;input = sys.stdin.readline
from collections import deque 
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

q = deque()
for i in range(n):
    if a[i] == 0:
        q.appendleft(b[i])
else:
    if not q:
        print(*c)
        exit(0)

for i in range(m):
    q.append(c[i])
    print(q.popleft(), end=' ')