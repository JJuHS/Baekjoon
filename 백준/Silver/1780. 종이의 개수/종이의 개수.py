import sys; input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = [0, 0, 0] #-1개수, 0개수, 1개수

def check(s, e):
    num = arr[s[0]][s[1]]
    for i in range(s[0], e[0] + 1):
        for j in range(s[1], e[1] + 1):
            if arr[i][j] != num:
                return False
    return True

def sol(s, e):
    if check(s, e):
        res[arr[s[0]][s[1]] + 1] += 1
        return
    l = (e[0] - s[0] + 1) // 3
    sol((s[0], s[1]), (s[0] + l-1, s[1] + l-1))
    sol((s[0], s[1]+l), (s[0] + l-1, s[1] + 2*l-1))
    sol((s[0], s[1]+2*l), (s[0] + l-1, s[1] + 3*l-1))

    sol((s[0]+l, s[1]), (s[0] + 2*l-1, s[1] + l-1))
    sol((s[0]+l, s[1]+l), (s[0] + 2*l-1, s[1] + 2*l-1))
    sol((s[0]+l, s[1]+2*l), (s[0] + 2*l-1, s[1] + 3*l-1))

    sol((s[0]+2*l, s[1]), (s[0] + 3*l-1, s[1] + l-1))
    sol((s[0]+2*l, s[1]+l), (s[0] + 3*l-1, s[1] + 2*l-1))
    sol((s[0]+2*l, s[1]+2*l), (s[0] + 3*l-1, s[1] + 3*l-1))

sol((0, 0), (n-1,n-1))
print('\n'.join(map(str, res)))