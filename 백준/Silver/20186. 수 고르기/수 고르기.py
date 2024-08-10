n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = -1e10
def sol(idx=0, cnt=0, ans=0, now=[]):
    global res
    if cnt == k:
        res = max(res, ans)
        return
    if k - cnt > n - idx:
        return
    for i in range(idx, n):
        sol(i + 1, cnt + 1, ans + arr[i] - cnt, now+[arr[i]])
sol()

print(res)