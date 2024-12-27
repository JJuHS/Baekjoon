import sys;input = sys.stdin.readline
from collections import defaultdict
from copy import deepcopy

Fields = [[0] * 4 for _ in range(4)]    # Fields[i][j] = i, j에 있는 물고기 번호, 없으면 0, 상어면 -1
Fishes = defaultdict(list)  # Fishes[i] = [x, y, d] -> i번 물고기의 정보 = 좌표, 방향
direction = [
    (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
]
res = 0

def input_data():
    for x in range(4):
        line  = list(map(int, input().split()))
        for j in range(4):
            index, d, y = line[j * 2], line[j * 2 + 1], j
            Fields[x][y] = index
            Fishes[index] = [x, y, d - 1]

def first_shark_move():
    global res
    fish_index = Fields[0][0]
    shark_d = Fishes[fish_index][2]
    res += fish_index
    del Fishes[fish_index]
    Fields[0][0] = -1
    return shark_d

def dfs(s_x, s_y, s_d, ans, fields, fishes):
    global res
    res = max(res, ans)
    # fish move
    for index_f in range(1, 17):
        if index_f not in fishes:continue
        x_f, y_f, nd_f = fishes[index_f]
        can_move = False
        # 이동불가능이면 방향 바꾸기
        for _ in range(8):
            nx_f, ny_f = x_f + direction[nd_f][0], y_f + direction[nd_f][1]
            if nx_f not in range(4) or ny_f not in range(4) or [nx_f, ny_f] == [s_x, s_y]:
                nd_f = (nd_f + 1) % 8
                continue
            can_move = True
            break
        if not can_move: continue
        # 이동
        other_index_f = fields[nx_f][ny_f]
        if other_index_f > 0:   # 이동하려는 곳에 다른 물고기 있음
            _, _, other_d_F = fishes[other_index_f]
            fields[x_f][y_f], fishes[other_index_f] = other_index_f, [x_f, y_f, other_d_F]
        else: # 이동하려는 곳에 다른 물고기 있음
            fields[x_f][y_f] = 0
        fields[nx_f][ny_f], fishes[index_f] = index_f, [nx_f, ny_f, nd_f]

    # shark move
    for power in range(1, 5):
        nx, ny = s_x + direction[s_d][0] * power, s_y + direction[s_d][1] * power
        if nx not in range(4) or ny not in range(4):break    # 경계 밖
        if fields[nx][ny] > 0:  # 물고기 있는 경우만 이동
            index_fish = fields[nx][ny]
            nd_x, nd_y, nd_s = fishes[index_fish]
            del fishes[index_fish]
            fields[nx][ny] = -1
            fields[s_x][s_y] = 0
            dfs(nx, ny, nd_s, ans + index_fish, deepcopy(fields), deepcopy(fishes))
            fields[s_x][s_y] = -1
            fishes[index_fish] = [nd_x, nd_y, nd_s]
            fields[nx][ny] = index_fish


input_data()
shark_d = first_shark_move()
dfs(0, 0, shark_d, res, Fields, Fishes)

print(res)