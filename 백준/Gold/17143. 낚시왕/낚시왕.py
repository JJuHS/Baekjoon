import sys; input = sys.stdin.readline

from collections import defaultdict

R, C, M = map(int, input().split())
fields = [[-1] * C for _ in range(R)]
sharks = defaultdict(int)
for shark_idx in range(M):
    r, c, s, d, z = map(int, input().split())
    fields[r - 1][c - 1] = shark_idx
    sharks[shark_idx] = (r - 1, c - 1, s, d, z)

# 낚시왕 우로 1보
man_r, man_c = 0, -1
def move_right():
    global man_c
    man_c += 1
    return

# 상어 잡기
res = 0
def fishing():
    global res
    for i in range(R):
        shark_idx = fields[i][man_c]
        if shark_idx == -1:continue
        else:
            shark = sharks[shark_idx]
            res += shark[4]
            del sharks[shark_idx]
            fields[i][man_c] = -1
            return

# 상어 이동 : 1상, 2하, 3우, 4좌
direction = [0, -1, 1, 1, -1]
def move_shark():
    new_fields = [[-1] * C for _ in range(R)]
    new_sharks = defaultdict(int)

    for shark_idx, shark in sharks.items():
        if not shark:continue
        r, c, s, d, z = shark
        # 상하 이동
        if d in [1, 2]:
            s %= 2 * (R - 1)
            nr = r + s * direction[d]
            if nr < 0:
                nr = -nr
                d = 2
            if nr >= R:
                nr = 2 * (R - 1) - nr
                d = 1
            if nr < 0:
                nr = -nr
                d = 2
            r = nr
        if d in [3, 4]:
            s %= 2 * (C - 1)
            nc = c + s * direction[d]
            if nc < 0:
                nc = -nc
                d = 3
            if nc >= C:
                nc = 2 * (C - 1) - nc
                d = 4
            if nc < 0:
                nc = -nc
                d = 3
            c = nc
            
        # 가려는데 다른 상어 없다
        if new_fields[r][c] == -1:
            new_fields[r][c] = shark_idx
            new_sharks[shark_idx] = (r, c, s, d, z)
        # 가려는데 다른 상어 있다
        else:
            other_idx = new_fields[r][c]
            if sharks[other_idx][4] < z:    # 지금 상어가 이기면
                new_fields[r][c] = shark_idx
                new_sharks[shark_idx] = (r, c, s, d, z)
                del new_sharks[other_idx]
                
    return new_sharks, new_fields

for _ in range(C):
    move_right()
    fishing()
    sharks, fields = move_shark()

print(res)