import sys
sys.setrecursionlimit(10**5)

res = set()
def dfs(n, x:str='9876543210'):
    global res
    if len(x) == n:
        res.add(int(x))
        return
    
    dfs(n, x[1:])
    dfs(n, x[:-1])
    if len(x) > 2:
        for i in range(1, len(x) - 1):
            dfs(n, x[:i] + x[i+1:])

for i in range(1, 11):
    dfs(i)

try:
    print(sorted(res)[int(input())])
except IndexError:
    print(-1)
