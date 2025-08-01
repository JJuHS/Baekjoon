import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    
visit = [0] * (n + 1)
now = 1

def dfs(x):
    global now
    visit[x] = now
    arr[x].sort()
    for a in arr[x]:
        if not visit[a]:
            now += 1
            dfs(a)
dfs(r)

for i in range(n):
    print(visit[i+1])
