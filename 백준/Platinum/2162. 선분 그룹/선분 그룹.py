import sys; input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(2 * n)]
parent = [i for i in range(2 * n)]
dp = [1 for i in range(2 * n)]
cnt = [False for i in range(2 * n)]


def union_find(x):
    if x == parent[x]: return x
    parent[x] = union_find(parent[x])
    return parent[x]


def union_set(x, y):
    x, y = union_find(x), union_find(y)
    if x == y: return 1
    if x < y:
        x, y = y, x
    parent[x] = y
    dp[y] += dp[x]
    return False


def ccw(a1, b1, a2, b2, a3, b3):
    return a1 * b2 + a2 * b3 + a3 * b1 - b1 * a2 - b2 * a3 - b3 * a1


def check(a, b):
    l1 = ccw(a[0], a[1], a[2], a[3], b[0], b[1]) * ccw(a[0], a[1], a[2], a[3], b[2], b[3])
    l2 = ccw(b[0], b[1], b[2], b[3], a[0], a[1]) * ccw(b[0], b[1], b[2], b[3], a[2], a[3])
    if l1 <= 0 and l2 <= 0:
        if l1 == 0 and l2 == 0:
            d1 = max(a[0], a[2]) >= min(b[0], b[2]) and max(b[0], b[2]) >= min(a[0], a[2])
            d2 = max(a[1], a[3]) >= min(b[1], b[3]) and max(b[1], b[3]) >= min(a[1], a[3])
            if d1 and d2:
                return 1
            return 0
        else:
            return 1
    return 0


for i in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    arr[2 * i] = (x1, y1)
    arr[2 * i + 1] = (x2, y2)
    union_set(2 * i, 2 * i + 1)

    for j in range(i):
        a = (x1, y1, x2, y2)
        b = (arr[2 * j][0], arr[2 * j][1], arr[2 * j + 1][0], arr[2 * j + 1][1])
        if check(a, b):
            union_set(2 * i, 2 * j)

group = []
for i in range(2 * n):
    if cnt[i]: continue
    a = union_find(i)
    group.append(a)
    for j in range(2 * n):
        if a == union_find(j): cnt[j] = 1

res = 0
for i in group: res = max(res, dp[i])

print(len(group))
print(res // 2)