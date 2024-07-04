from itertools import combinations as cb
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
chicken = []
house = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(n):
        if tmp[j] == 2:
            chicken.append((i, j))
        if tmp[j] == 1:
            house.append((i, j))

res = 10**6
for chicks in cb(chicken, m):
    tmp = 0
    for j in range(len(house)):
        dist_tmp = 10**6
        for chick in chicks:
            dist_tmp = min(dist_tmp, abs(chick[0] - house[j][0]) + abs(chick[1] - house[j][1]))
        tmp += dist_tmp
    res = min(res, tmp)
print(res)