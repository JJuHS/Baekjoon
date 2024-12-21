import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline

masking = 1 << 10
div = 10 ** 9

def sol(n: int):
    dp = [[[0] * masking for _ in range(10)] for _ in range(n + 1)]

    for i in range(1, 10):
        dp[1][i][1 << i] = 1

    for i in range(1, n):
        for j in range(10):
            for k in range(masking):
                if j > 0:
                    dp[i + 1][j - 1][k | (1 << (j - 1))] += dp[i][j][k]
                    dp[i + 1][j - 1][k | (1 << (j - 1))] %= div
                if j < 9:
                    dp[i + 1][j + 1][k | (1 << (j + 1))] += dp[i][j][k]
                    dp[i + 1][j + 1][k | (1 << (j + 1))] %= div

    res = 0
    for i in range(10):
        res += dp[n][i][masking - 1]
        res %= div

    print(res)

sol(int(input()))
