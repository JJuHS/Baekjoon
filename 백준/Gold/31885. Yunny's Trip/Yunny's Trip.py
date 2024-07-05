import sys; input = sys.stdin.readline
n, k = map(int, input().split()) # 아이템 개수, 기력
items = [tuple(map(int, input().split())) for _ in range(n)] # 아이템
goal_x, goal_y = map(int, input().split()) # 목적지

res = abs(goal_x) + abs(goal_y)

res_set = set()

for x, y in items:
    res_set.add((goal_x - x, goal_y - y))

for x, y in items:
    res = min(res, abs(goal_x - x) + abs(goal_y -y) + 2)
    if (x, y) in res_set: res = min(res, 4)
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if (x + dx, y + dy) in  res_set: res = min(res, 5)

print(res if res <= k else -1)