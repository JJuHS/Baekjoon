from collections import deque as dq
n, m = map(int,input().split())
arr = []
for i in range(n):
    tmp = list(map(str,input()))
    arr.append(tmp)
    for j in range(m):
        if tmp[j] == 'R':
            rsx, rsy = i, j
        if tmp[j] == 'B':
            bsx, bsy = i, j
        if tmp[j] == 'O':
            ox, oy = i, j

def move(x, y, dx, dy):
    cnt = 0
    nx, ny = x, y
    while arr[nx + dx][ny + dy] != '#' and arr[nx][ny] != 'O':
        nx += dx
        ny += dy
        cnt += 1
    return nx,  ny, cnt

s = dq()
def solution():
    visited = {}
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    s.append([rsx, rsy, bsx, bsy, 0])

    while s:
        rx, ry, bx, by, cnt = s.popleft()
        if cnt >= 10:
            return -1

        for dx, dy in direction:
            rrx, rry, rcnt = move(rx, ry, dx, dy)
            bbx, bby, bcnt = move(bx, by, dx, dy)

            if arr[bbx][bby] != 'O':
                if rrx == ox and rry == oy:
                    return cnt + 1

                if rrx == bbx and rry == bby:
                    if rcnt > bcnt:
                        rrx, rry = rrx - dx, rry - dy
                    else:
                        bbx, bby = bbx - dx, bby - dy

                if (rrx, rry, bbx, bby) in visited:
                    continue
                else:
                    visited[(rrx, rry, bbx, bby)] = 1
                    s.append([rrx, rry, bbx, bby, cnt+1])
    return -1

print(solution())