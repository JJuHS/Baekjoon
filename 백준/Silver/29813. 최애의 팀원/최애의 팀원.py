from collections import deque as dq

n = int(input())
q = dq()

for _ in range(n):
    x, y = map(str, input().split())
    y = int(y) % 100
    q.append((x, y))

def my_mate():
    while True:
        if len(q) == 1:
            return
        now = q.popleft()
        cnt = 0
        while True:
            tmp = q.popleft()
            if now[1] == 1 + cnt:
                break
            q.append(tmp)
            cnt += 1
my_mate()
print(q[0][0])