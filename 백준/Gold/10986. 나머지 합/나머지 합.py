import sys;input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0] * m
now = 0
for i in range(n):
    now = (now + arr[i]) % m
    cnt[now] += 1

res = cnt[0]

for i in cnt:
    res += i * (i - 1) // 2

print(res)