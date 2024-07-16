import sys;input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
ans1, ans2 = 0, []

for i in range(n):
    tmp = sorted([arr[j][i] for j in range(m)])
    c = tmp[m // 2]
    ans1 += sum([abs(tmp[k] - c) for k in range(m)])
    ans2.append(c)

print(ans1)
print(*ans2)
