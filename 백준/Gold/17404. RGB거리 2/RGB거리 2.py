import sys; input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def sol(x):
    global res
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = arr[0]

    for j in range(3):
        if j == x:
            dp[1][j] = 1e9
            continue
        dp[1][j] = arr[1][j] + arr[0][x]

    for j in range(2, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + arr[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + arr[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + arr[j][2]

    dp[n - 1].pop(x)
    res = min(*dp[n - 1], res)
    return


res = 1e10
sol(0); sol(1); sol(2)

print(res)