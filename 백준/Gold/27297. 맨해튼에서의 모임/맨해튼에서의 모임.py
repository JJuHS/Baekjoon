import sys; input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
ans = [0, []]


def sol(i, idx=0):
    tmp = []
    for j in range(m):
        tmp.append(arr[j][i])
    tmp.sort()
    now = tmp[0]
    res = [sum([abs(tmp[k] - tmp[m//2]) for k in range(m)]), tmp[m//2]]
    ans[0] += res[0]
    ans[1].append(res[1])
    return


for a in range(n):
    sol(a)
print(ans[0])
print(*ans[1])
