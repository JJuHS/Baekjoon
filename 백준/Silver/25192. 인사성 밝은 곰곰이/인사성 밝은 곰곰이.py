import sys; input = sys.stdin.readline
res, cnt = set(), 0
for _ in range(int(input())):
    a = input().strip()
    if a == 'ENTER':
        res.clear()
        continue
    if a not in res:
        res.add(a)
        cnt += 1

print(cnt)