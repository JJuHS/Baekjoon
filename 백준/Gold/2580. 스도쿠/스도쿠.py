# # s 4명 이상 / 가로 세로 인점 / 7명
# from collections import deque
# mate = [list(input()) for _ in range(5)]
# direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
sdoku = []
empty = []
row = [[0] * 10 for _ in range(9)]
col = [[0] * 10 for _ in range(9)]
square = [[0] * 10 for _ in range(9)]

for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if not tmp[j]:
            empty.append((i, j))
        else:
            k = tmp[j]
            row[i][k] = col[j][k] = square[i // 3 * 3 + j // 3][k] = 1
    sdoku.append(list(tmp))

def sol(s = 0):
    if s == len(empty):
        for i in range(9):
            print(*sdoku[i])
        exit(0)
    x, y = empty[s]
    for k in range(1, 10):
        if not row[x][k] + col[y][k] + square[x // 3 * 3 + y // 3][k]:
            sdoku[x][y] = k
            row[x][k] = col[y][k] = square[x // 3 * 3 + y // 3][k] = 1
            if sol(s + 1): return True
            sdoku[x][y] = 0
            row[x][k] = col[y][k] = square[x // 3 * 3 + y // 3][k] = 0
    return False
sol()
for i in range(9):
    print(*sdoku[i], ' ')
