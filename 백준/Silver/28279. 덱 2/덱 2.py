import sys;input = sys.stdin.readline
from collections import deque as dq
n = int(input())
q = dq([])
for _ in range(n):
    s = input().strip()
    c = s[0]
    if c == '1':q.appendleft(s[2:])
    if c == '2':q.append(s[2:])
    if c == '3':print(q.popleft() if q else -1)
    if c == '4':print(q.pop() if q else -1)
    if c == '5':print(len(q))
    if c == '6':print(int(len(q) == 0))
    if c == '7':print(q[0] if q else -1)
    if c == '8':print(q[-1] if q else -1)    