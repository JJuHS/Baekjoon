import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())
high_air = 0
low_air = 0
arr = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if arr[i][0] == -1:
        high_air = i
        low_air = i + 1
        arr[i][0] = arr[i + 1][0] = 0
        break


def diffusion():
    diffused_tmp = [[0] * c for _ in range(r)]
    remained_tmp = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y] > 0:
                amount = arr[x][y] // 5
                cnt = 0
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if nx in range(r) and ny in range(c):
                        if ny == 0 and nx in [high_air, low_air]:
                            continue
                        diffused_tmp[nx][ny] += amount
                        remained_tmp[x][y] += amount
    for i in range(r):
        for j in range(c):
            arr[i][j] += diffused_tmp[i][j] - remained_tmp[i][j]


def air_cleaner():
    # high
    for i in range(high_air - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]
    for i in range(c - 1):
        arr[0][i] = arr[0][i + 1]
    for i in range(high_air):
        arr[i][c - 1] = arr[i + 1][c - 1]
    for i in range(c - 1, 0, -1):
        arr[high_air][i] = arr[high_air][i - 1]
    arr[high_air][0] = 0
    # low
    for i in range(low_air, r - 1):
        arr[i][0] = arr[i + 1][0]
    arr[low_air][0] = 0
    for i in range(c - 1):
        arr[r - 1][i] = arr[r - 1][i + 1]
    for i in range(r - 1, low_air, -1):
        arr[i][c - 1] = arr[i - 1][c - 1]
    arr[low_air][0] = 0
    for i in range(c - 1, 0, -1):
        arr[low_air][i] = arr[low_air][i - 1]
    arr[low_air][0] = 0


for _ in range(t):
    diffusion()
    air_cleaner()
print(sum(sum(arr, [])))