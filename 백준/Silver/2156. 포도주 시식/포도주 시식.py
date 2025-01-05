import sys
input = sys.stdin.readline

n = int(input())

dp = [[0, 0, 0] for _ in range(n)]

# 안먹음, 1잔째, 2잔째

for i in range(n):
    now = int(input())
    if i == 0:
        dp[i] = [0, now, now]
        continue
    if i == 1:
        dp[i] = [dp[0][1], now, now + dp[0][1]]
        continue
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = now + max(dp[i - 1][0], max(dp[i - 2]))
    dp[i][2] = now + dp[i - 1][1]

print(max(dp[-1]))