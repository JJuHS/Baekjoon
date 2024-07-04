n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def sol(now=0, res=[]):
    if len(res) == m:
        print(*res)
        return
    for i in range(now, n):
        tmp = arr[i]
        sol(i, res + [tmp])



sol()