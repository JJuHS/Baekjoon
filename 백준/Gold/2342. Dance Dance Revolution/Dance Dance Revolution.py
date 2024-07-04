import sys; input = sys.stdin.readline
arr = list(map(int, input().split()))
n, inf, res = len(arr), 1e10, 1e10


def dist(x, y):
    if x==y: return 1
    if x == 0: return 2
    if (x - y) % 2: return 3
    return 4

# dp -> n번째 힘, 왼발위치, 오른발 위치
dp = [[[inf for _1 in range(5)] for _2 in range(5)] for _3 in range(n + 1)]
dp[0][0][0] = 0
for i in range(1, n):
    cmd = arr[i - 1]
    for left in range(5):
        for right in range(5):
            dp[i][cmd][right] = min(dp[i][cmd][right], dp[i - 1][left][right] + dist(left, cmd))
            dp[i][left][cmd] = min(dp[i][left][cmd], dp[i - 1][left][right] + dist(right, cmd))

for i in range(5):
    for j in range(5):
        res = min(res, dp[n - 1][i][j])

print(res)