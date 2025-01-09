import sys;input = sys.stdin.readline

n, k = map(int, input().split())
dp = [1] + [0] * k  # dp[i] : i원을 만드는 경우의 수

for coin in [int(input()) for _ in range(n)]:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])