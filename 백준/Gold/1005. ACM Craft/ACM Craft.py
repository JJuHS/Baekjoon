from collections import deque as dq
T  = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    spend_time = [0] + list(map(int, input().split()))
    need = [[] * n for _ in range(n + 1)]
    for i in range(k):
        x, y = map(int, input().split())
        need[y].append(x)
    w = int(input())
    q = dq()
    total_time = [0] * (n + 1)
    for i in range(n + 1):
        if not need[i]:
            q.append(i)
            total_time[i] = spend_time[i]
    while q:
        now = q.popleft()
        time = total_time[now]
        for i in range(1, n + 1):
            if now in need[i]:
                need[i].remove(now)
                if not need[i]:
                    q.append(i)
                total_time[i] = max(total_time[i], time + spend_time[i])

    print(total_time[w])

