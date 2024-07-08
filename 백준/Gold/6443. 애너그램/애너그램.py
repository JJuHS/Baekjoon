import sys; input = sys.stdin.readline
n = int(input())


def sol(cnt):
    if cnt == len(s):
        print(''.join(res))
        return
    
    for i in visit:
        if visit[i]:
            visit[i] -= 1
            res.append(i)
            sol(cnt + 1)
            visit[i] += 1
            res.pop()


for i in range(n):
    s = sorted(list(input().strip()))
    visit = {}
    for i in s:
        if i not in visit:
            visit[i] = 1
        else:
            visit[i] += 1
    res = []
    sol(0)


