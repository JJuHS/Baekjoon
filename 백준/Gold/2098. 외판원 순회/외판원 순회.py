import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline
inf = 1e10

n = int(input())    # 2 < n < 16

arr = [list(map(int, input().split())) for _ in range(n)]   # 비대칭 그래프
dp = [[-1] * (1 << n) for _ in range(n)] # dp[i][j] : i 에 도달, k = visited인 최소 비용

def dfs(now, visit):
    if visit == (1 << n) - 1:   # 모든 도시 방문
        return arr[now][0] if arr[now][0] > 0 else inf

    # 최소비용 이미 있음 -> 재사용
    if dp[now][visit] != -1: return dp[now][visit] 

    dp[now][visit] = inf
    for next in range(1, n):
        if arr[now][next] == 0:continue # 경로가 없음
        if visit & (1 << next):continue    # 이미 방문함

        # 점화식 - 재귀
        # 1. 현위치(now)에서 다음도시(next)로 이동
        # 2. 방문처리, 최소비용 있는 경우 이미 위에서 체크함
        # 3. dfs + 재귀 -> 비용 갱신
        dp[now][visit] = min(
            dp[now][visit], 
            arr[now][next] + dfs(next, visit | (1 << next))
            )

    return dp[now][visit]

# 사이클이기 때문에 시작을 0으로, 0을 방문 -> visit = 1
res = dfs(0, 1)  

print(res)
