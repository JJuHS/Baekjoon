import sys;input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
res = [[sum([A[i][j] * B[j][k] for j in range(M)]) for k in range(K)] for i in range(N)]

for i in range(N):print(*res[i])