import sys; input = sys.stdin.readline
direction = {}
direction['D'] = [0, 1]
direction['L'] = [-1, 0]
direction['R'] = [1, 0]
direction['U'] = [0, -1]
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
parent = [i for i in range(n * m)]


def union_find(x):
    if x == parent[x]: return x
    parent[x] = union_find(parent[x])
    return parent[x]


def union_set(x, y):
    x, y = union_find(x), union_find(y)
    if x == y: return
    if x < y: parent[y] = x
    else: parent[x] = y


for idx in range(n * m):
    x = idx % m
    y = idx // m
    tmp = arr[y][x]
    nx = x + direction[tmp][0]
    ny = y + direction[tmp][1]
    next_num = ny * m + nx
    if next_num < 0 or next_num >= n * m: continue
    union_set(idx, next_num)

res = 0
visited = {}
for i in range(n * m):
    if union_find(parent[i]) not in visited:
        res += 1
        visited[parent[i]] = 1

print(res)