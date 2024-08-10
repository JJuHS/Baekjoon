import sys
input = sys.stdin.readline
n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
find = {}
ans = 0
for i in range(n):
    find[i] = 0
    find[-i] = 0

def bishop(idx):
    ans_tmp = 0
    for dist in range(idx, 2 * n - 1):
        for j in range(dist + 1):
            k = dist - j
            if 0<= j < n and 0<= k < n and not find[j - k]:
                ans_tmp += 1
                break
    return ans_tmp

def bfs(idx_ = 0, cnt = 0):
    global ans
    if idx_ == 2 * n - 1:
        ans = max(ans, cnt)
        return
    s_tmp = bishop(idx_)
    if s_tmp + cnt <= ans:
        return
    for tmp_x in range(idx_ + 1):
        tmp_y = idx_ - tmp_x
        if 0 <= tmp_x < n and 0 <= tmp_y < n and chess[tmp_x][tmp_y] and not find[tmp_y - tmp_x]:
            find[tmp_y - tmp_x] = 1
            bfs(idx_ + 1, cnt + 1)
            find[tmp_y - tmp_x] = 0
    bfs(idx_ + 1, cnt)

bfs()
print(ans)