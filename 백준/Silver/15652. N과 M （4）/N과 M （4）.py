n, m = map(int, input().split())


def sol(now=1, res=[]):
    if len(res) == m:
        print(*res)
        return
    for i in range(now, n + 1):
        sol(i, res + [i])



sol()