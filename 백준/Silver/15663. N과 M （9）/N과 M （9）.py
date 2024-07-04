n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = 0
ans = []
visit = [0] * n
def dfs(c=0):
    tmp = 0
    if c == m:
        print(*ans)
    for i in range(n):
        if arr[i] != tmp and not visit[i]:
            ans.append(arr[i])
            tmp = arr[i]
            visit[i] = 1
            dfs(c+1)
            visit[i] = 0
            ans.pop()
dfs()