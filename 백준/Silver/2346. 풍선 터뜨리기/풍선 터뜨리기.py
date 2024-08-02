from collections import deque as dq
n = int(input())
res = []
arr = list(map(int, input().split()))
q = dq([(i, arr[i]) for i in range(n)])
while q:
    idx, num = q.popleft()
    res.append(idx + 1)
    q.rotate(-num)
    if num > 0:
        q.rotate(1)

print(*res)
