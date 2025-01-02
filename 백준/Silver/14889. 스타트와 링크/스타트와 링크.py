import sys; input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

res = 100000
visit = [0] * n

def sol(left:list=[], now:int=0, cnt:int=0):
    global res
    if len(left) == n // 2:
        res = min(res, find_diff(left, [i for i in range(n) if not visit[i]]))
        return
    for i in range(now, n):
        if i in visit:continue

        visit[i] = 1
        sol(left + [i], i + 1, cnt + 1)
        visit[i] = 0

def find_diff(l, r):
    diff = 0
    for i in range(n // 2):
        for j in range(i, n // 2):
            if i != j:
                diff += arr[l[i]][l[j]] + arr[l[j]][l[i]] - arr[r[i]][r[j]] - arr[r[j]][r[i]]
    return abs(diff)

sol()
print(res)