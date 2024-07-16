import sys; input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
ans1, ans2 = 0, []

for i in range(n):
    tmp = [arr[j][i] for j in range(m)]
    tmp.sort()
    ans1 += sum([abs(tmp[k] - tmp[m//2]) for k in range(m)])
    ans2.append(tmp[m//2])
    
print(ans1)
print(*ans2)
