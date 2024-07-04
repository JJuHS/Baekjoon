n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
n = len(arr)
def sol(now=0, res=[]):
    if len(res) == m:
        print(*res)
        return
    for i in range(now, n):
        tmp = arr[i]
        sol(i, res + [tmp])



sol()