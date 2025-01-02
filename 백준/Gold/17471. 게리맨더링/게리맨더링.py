import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque as dq

n = int(input())
populations = list(map(int, input().split()))
arr = [[0] * n for _ in range(n)]

for i in range(n):
    inp = list(map(int, input().split()))
    num = inp[0]
    for j in range(1, num + 1):
        arr[i][inp[j] - 1] = 1
        arr[inp[j] - 1][i] = 1

inf = 1e10
res = inf
total = sum(populations)

def sol(left:list):
    global res
    right = [i for i in range(n) if i not in left]
    
    if len(left) in [0, n]:return
    if not check(left, len(left)):return
    if not check(right, len(right)):return

    res = min(res, abs(total - 2 * sum([populations[i] for i in left])))


def check(x:list, d:int):
    q = dq()
    visit = [0] * len(x)
    visit[0] = 1
    q.append(0)

    while q:
        now = q.popleft()
        for i in range(len(x)):
            if visit[i] or not arr[x[now]][x[i]]:continue
            visit[i] = 1
            q.append(i)

    return False if 0 in visit else True

for i in range(1 + n // 2):
    for com in combinations([j for j in range(n)], i):
        sol(list(com))

print(res if res != inf else -1)
