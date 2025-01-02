import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[1, arr[i]] for i in range(n)] # 개수, 최대크기

for i in range(1, n):
    for j in range(i):
        if arr[i] <= arr[j]:continue # 박스 크기 불가능
        if dp[j][0] < dp[i][0]:continue # 이미 개수 많음
        dp[i][0] = dp[j][0] + 1

res = max([dp[i][0] for i in range(n)])
print(res)