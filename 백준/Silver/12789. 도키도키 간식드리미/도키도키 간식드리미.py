from collections import deque as dq
n = int(input())
q = dq(list(map(int, input().split())))
stack = []
t = 1
res = 'Sad'

while True:
    if stack and stack[-1] == t:
                now = stack.pop()
                t += 1
    elif q[0] == t:
        now = q.popleft()
        t += 1
    else:
        now = q.popleft()
        if stack and stack[-1] < now:
            break
        stack.append(now)
    if t == n:
        res = 'Nice'
        break

print(res)

