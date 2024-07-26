import sys
N, M, B = map(int, sys.stdin.readline().split())
Block_ = []
for _ in range(N):
    Block_ += list(map(int, sys.stdin.readline().split()))
height = 0
n = N * M
ans = 1e10
ans_list = [ans]

for ground in range(257):
    if len(ans_list) > 1:
        if ans_list[-1] > ans_list[-2]:
            break

    up = 0
    down = 0

    for i in range(n):
        if Block_[i] > ground:
            up += Block_[i] - ground
            continue
        down += ground - Block_[i]

    if up + B < down:
        break

    if down + 2 * up <= ans:
        ans = down + 2 * up
        height = ground
        ans_list.append(ans)

print(ans, height)
