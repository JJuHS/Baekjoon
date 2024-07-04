import sys
input = sys.stdin.readline
inf = 1e10


def sol(start=1):
    dp = [inf for _ in range(n + 1)]
    dp[start] = 0
    for idx in range(n):
        for s in start_li:
            for e, t in arr[s]:
                if dp[e] > dp[s] + t:
                    if idx == n - 1:
                        return True
                    dp[e] = dp[s] + t
    return False


T = int(input())
for _ in range(T):
    n, m, w = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    start_li = set()

    for _ in range(m):
        s, e, t = map(int, input().split())
        arr[s].append([e, t])
        arr[e].append([s, t])
        start_li.add(s)
        start_li.add(e)
    for _ in range(w):
        s, e, t = map(int, input().split())
        arr[s].append([e, -t])
        start_li.add(s)
    start_li = list(start_li)

    res = sol()
    print(['NO', 'YES'][res])

