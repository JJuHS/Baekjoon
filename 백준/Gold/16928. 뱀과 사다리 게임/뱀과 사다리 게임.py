# import sys
# input = sys.stdin.readline
from collections import deque as dq
n, m = map(int, input().split())
ladder = {}
snake = {}
ans = [0] * 101
visit = [0] * 101

for i in range(n):
    x, y =  map(int, input().split())
    ladder[x] = y
for i in range(m):
    u, v =  map(int, input().split())
    snake[u] = v

q = dq([1])
def bfs():
    while q:
        now = q.popleft()
        for dice in range(1, 7):
            next = now + dice
            if next <= 100 and not visit[next]:
                tmp = next
                if next in ladder:
                    tmp = ladder[next]
                if next in snake:
                    tmp = snake[next]
                if tmp == 100:
                    return 1 + ans[now]
                if not visit[tmp]:
                    visit[tmp] = 1
                    ans[tmp] = ans[now] + 1
                    q.append(tmp)

print(bfs())