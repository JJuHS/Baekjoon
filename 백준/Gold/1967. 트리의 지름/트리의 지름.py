import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append([c, w])
    graph[c].append([p, w])


def dfs(x = 1, dist=0):
    for end, weight in graph[x]:
        if ans[end] == -1:
            ans[end] = dist + weight
            dfs(end, dist + weight)

ans = [-1] * (n + 1)
ans[1] = 0
dfs()
start = ans.index(max(ans))

ans = [-1] * (n + 1)
ans[start] = 0

dfs(start)
print(max(ans))
