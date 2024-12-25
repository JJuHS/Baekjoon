import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline

from collections import deque as dq

s = list(input().strip())
l = len(s)
dp_pldm = [[0] * l for j in range(l)] # dp_pldm[i][j] = i인덱스 ~ j인덱스가 팰린드롬 인가?

dp_pldm[0][0] = 1
for i in range(1, l):
    dp_pldm[i][i] = 1    # 길이 1 팰린드롬
    if s[i] == s[i - 1]:
        dp_pldm[i - 1][i] = 1  # 길이 2 팰린드롬

for k in range(3, l + 1):   # 길이 3이상 팰린드롬 찾기
    for i in range(l - k + 1):  # 길이 k, 시작점 i
        j = i + k - 1
        if s[i] == s[j] and dp_pldm[i + 1][j - 1]:
            dp_pldm[i][j] = 1

dp_res = [0] * (l) # 0 ~ i 까지 분할 최소값

for j in range(l):  # 끝점 j
    for i in range(j + 1):  # 시작점 i
        if dp_pldm[i][j]:
            if dp_res[j] and dp_res[j] <= dp_res[i - 1]:continue
            dp_res[j] = dp_res[i - 1] + 1

print(dp_res[l - 1])