import sys;input = sys.stdin.readline

for _ in range(int(input())):
    n, l, r = map(float, input().split())
    n = int(n)

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[0][i] = i
    for i in range(1, n + 1):
        for j in range(n):
            dp[i][j] = l * (dp[i-1][j+1] - 1) + (1 - r - l) * dp[i-1][j] + r * (dp[i-1][max(0, j-1)] + 1)
        
    print(f'{dp[n][0]:.4f}')