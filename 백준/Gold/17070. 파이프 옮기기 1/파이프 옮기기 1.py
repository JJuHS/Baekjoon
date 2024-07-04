import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

# 0 : 가로, 1: 대각선, 2 : 세로
def sol():
    dp[0][0][1] = 1
    for i in range(2, n):
        if not arr[0][i]:
            dp[0][0][i] = dp[0][0][i - 1]

    for x in range(1, n):
        for y in range(1, n):
            if not arr[x][y] + arr[x - 1][y] + arr[x][y - 1]:
                dp[1][x][y] = dp[0][x - 1][y - 1] + dp[1][x - 1][y - 1] + dp[2][x -1][y - 1]
            if not arr[x][y]:
                dp[2][x][y] = dp[1][x - 1][y] + dp[2][x - 1][y]
                dp[0][x][y] = dp[0][x][y - 1] + dp[1][x][y - 1]

sol()
print(dp[0][-1][-1] + dp[1][-1][-1] + dp[2][-1][-1])
