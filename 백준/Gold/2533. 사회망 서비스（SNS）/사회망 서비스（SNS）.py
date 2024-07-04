from collections import deque as dq
import sys; input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visit = [0 for _ in range(n + 1)]
adapted = [0 for _ in range(n + 1)]
q = dq()

for i in range(1, n + 1):
    if len(tree[i]) == 1:
        q.append(i)
        visit[i] = 1

while q:
    now = q.popleft()
    if not tree[now]:
        continue
    leaf = tree[now].pop()
    tree[leaf].remove(now)
    if len(tree[leaf]) == 1:
        q.append(leaf)
    if adapted[now]:
        continue
    adapted[leaf] = 1

print(sum(adapted))