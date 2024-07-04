import sys
input = sys.stdin.readline
n, c = map(int, input().split())
home = sorted([int(input()) for _ in range(n)])
total = len(home)

s = 1
e = home[-1] - home[0]
res = 0

while e >= s:
    mid = (s + e) // 2
    now = home[0]
    cnt = 1
    for i in range(1, total):
        if home[i] >= now + mid:
            cnt += 1
            now = home[i]
    if cnt >= c:
        s = mid + 1
        res = mid
    else:
        e = mid - 1

print(res)