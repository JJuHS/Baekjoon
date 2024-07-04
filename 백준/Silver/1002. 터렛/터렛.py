import sys
T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    ans = 2
    if dist == r1 + r2:
        ans = 1
    if dist == abs(r1 - r2):
        ans = 1
    if dist > r1 + r2:
        ans = 0
    if dist < abs(r1-r2):
        ans = 0
    if r1 == r2 and x1 == x2 and y1 == y2:
        ans = -1
    if r1 != r2 and x1 == x2 and y1 == y2:
        ans = 0
    print(ans)