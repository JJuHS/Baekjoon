from collections import defaultdict
import sys;input=sys.stdin.readline
n, m = map(int, input().split())
res = defaultdict(int)
for _ in range(n):
    a = input().strip()
    if len(a) >= m:
        res[a] += 1

arr = list(res.keys())
arr.sort(key=lambda x : (-res[x], -len(x), x))
print('\n'.join(arr))