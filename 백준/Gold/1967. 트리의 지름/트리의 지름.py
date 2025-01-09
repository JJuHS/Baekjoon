import sys;input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    graph[p].append([c, w])
    graph[c].append([p, w])

def dfs(x:int=1, d:int=0):
    for e, w in graph[x]:
        if ans[e] == -1:
            ans[e] = d + w
            dfs(e, d + w)

ans = [-1] * (n + 1)
ans[1] = 0
dfs()
s = ans.index(max(ans))

ans = [-1] * (n + 1)
ans[s] = 0
dfs(s)

print(max(ans))
