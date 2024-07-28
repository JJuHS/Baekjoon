x, n, res = int(input()), int(input()), 0
for _ in range(n):
    a,b=map(int,input().split())
    res += a*b
print(['No', 'Yes'][res==x])