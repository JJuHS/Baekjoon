import sys
n = int(input())
friends = [sys.stdin.readline().strip() for _ in range(n)]
ans = 0
for i in range(n):
    friends2 = set()
    for j in range(n):
        if friends[i][j] == 'N': continue
        friends2.add(j)
        for k in range(n):
            if friends[j][k] == 'N': continue
            friends2.add(k)
    ans = max(ans, len(friends2)-1)
print(ans)

