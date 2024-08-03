import sys;input=sys.stdin.readline
n = int(input())
res = ['ChongChong']
for _ in range(n):
    a, b = map(str, input().split())
    if a in res and b not in res:
        res.append(b)
    if b in res and a not in res:
        res.append(a)
print(len(res))