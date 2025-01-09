import sys;input = sys.stdin.readline

def sol(arr:list, k:int):
    prefix_sum = [0] * (k + 1)
    for i in range(k):prefix_sum[i+1]=prefix_sum[i]+arr[i]   # 누적합
    
    dp = [[0] * k for _ in range(k)]    # dp[i][j] : i부터 j까지 합치는 최솟값
    for i in range(k-1):dp[i][i+1] = arr[i]+arr[i+1]
    
    for l in range(2, k):  # 구간의 길이
        for i in range(k - l):  # 시작점
            j = i + l   # 끝점
            dp[i][j] = min(
                [float('inf')] + 
                [dp[i][p] + dp[p+1][j] for p in range(i, j)]
            )
            dp[i][j] += prefix_sum[j + 1] - prefix_sum[i]
    
    print(dp[0][k-1])


for _ in range(int(input())):
    k = int(input())
    arr = list(map(int, input().split()))
    sol(arr, k)