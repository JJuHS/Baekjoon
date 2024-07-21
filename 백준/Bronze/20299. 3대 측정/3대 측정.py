import sys; input = sys.stdin.readline
n, k, l = map(int, input().split())
res, arr = 0, []
for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= k:
        if a >= l and b >= l and c >= l:
            res += 1
            arr += [a, b, c]

print(res)
print(*arr)