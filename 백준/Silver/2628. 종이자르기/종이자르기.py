import sys; input=sys.stdin.readline
n, m = map(int, input().split())
res1, res2 = [0,n], [0,m]
for _ in range(int(input())):
    c, w = map(int, input().split())
    if c == 1:res1.append(w)
    else:res2.append(w)
res1.sort()
res2.sort()
print(max([res1[i] - res1[i - 1] for i in range(1, len(res1))]) * max([res2[j] - res2[j - 1] for j in range(1, len(res2))]))