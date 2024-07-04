import sys; input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n)]

def union_find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union_set(x, y):
    x, y = union_find(x), union_find(y)
    if x < y: parent[y] = x
    else: parent[x] = y

res = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())
    if union_find(a) == union_find(b):
        res = i
        break
    union_set(a, b)

print(res)