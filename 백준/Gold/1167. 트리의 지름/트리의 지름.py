from collections import deque as dq
import sys; input = sys.stdin.readline

def bfs(v, arr, s):
    q = dq()
    q.append((s, 0))
    visit = [-1] * (v + 1)
    visit[s] = 0
    res = [0, 0]

    while q:
        now, dist = q.popleft()
        for n_next, dist_next in arr[now]:
            if visit[n_next] == -1:
                sum_dist = dist + dist_next
                q.append((n_next, sum_dist))
                visit[n_next] = sum_dist
                if res[1] < sum_dist:
                    res[0], res[1] = n_next, sum_dist
    return res

v = int(input())
arr = [[] for _ in range(v + 1)]

for _ in range(v):
    graph = list(map(int, input().split()))
    v_cur = graph[0]
    i = 1
    while True:
        if graph[i] == -1:break
        e, w = graph[i], graph[i + 1]
        arr[v_cur].append((e, w))
        i += 2

print(bfs(v, arr, bfs(v, arr, 1)[0])[1])