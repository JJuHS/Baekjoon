import sys
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
res = 0

if n == 1:
    print(game[0][0])
    exit(0)

def left(brd):
    for i in range(n):
        now = 0
        for j in range(1, n):
            if brd[i][j] != 0:
                tmp = brd[i][j]
                brd[i][j] = 0

                if brd[i][now] == 0:
                    brd[i][now] = tmp

                elif brd[i][now] == tmp:
                    brd[i][now] *= 2
                    now += 1
                else:
                    now += 1
                    brd[i][now] = tmp

    return brd

def right(brd):
    for i in range(n):
        now = n - 1
        for j in range(n - 1, -1, -1):

            if brd[i][j] != 0:
                tmp = brd[i][j]
                brd[i][j] = 0

                if brd[i][now] == 0:
                    brd[i][now] = tmp

                elif brd[i][now] == tmp:
                    brd[i][now] *= 2
                    now -= 1
                else:
                    now -= 1
                    brd[i][now] = tmp
    return brd

def up(brd):
    for j in range(n):
        now = 0
        for i in range(n):
            if brd[i][j] != 0:
                tmp = brd[i][j]
                brd[i][j] = 0

                if brd[now][j] == 0:
                    brd[now][j] = tmp

                elif brd[now][j] == tmp:
                    brd[now][j] *= 2
                    now += 1

                else:
                    now += 1
                    brd[now][j] = tmp
    return brd

def down(brd):
    for j in range(n):
        now = n - 1
        for i in range(n - 1, -1, -1):
            if brd[i][j] != 0:
                tmp = brd[i][j]
                brd[i][j] = 0

                if brd[now][j] == 0:
                    brd[now][j] = tmp

                elif brd[now][j] == tmp:
                    brd[now][j] *= 2
                    now -= 1

                else:
                    now -= 1
                    brd[now][j] = tmp
    return brd

def dfs(c, arr):
    global res
    if c == 5:
        res = max(max(map(max, *arr)), res)
        return
    for i in range(4):
        copy_arr = deepcopy(arr)
        if i == 0:
            dfs(c + 1, left(copy_arr))
        elif i == 1:
            dfs(c + 1, right(copy_arr))
        elif i == 2:
            dfs(c + 1, up(copy_arr))
        else:
            dfs(c + 1, down(copy_arr))

dfs(0, game)
print(res)