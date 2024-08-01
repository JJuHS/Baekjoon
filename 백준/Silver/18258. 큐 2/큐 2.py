import sys;input = sys.stdin.readline
from collections import deque as dq
n = int(input())
q = dq([])
for _ in range(n):
    s = input().strip()
    if s[:4] == 'push':q.append(s[5:])
    if 'pop' == s:print(q.popleft() if q else -1)
    if 'size' == s:print(len(q))
    if 'empty' == s:print(int(len(q) == 0))
    if 'front' == s:print(q[0] if q else -1)
    if 'back' == s:print(q[-1] if q else -1)