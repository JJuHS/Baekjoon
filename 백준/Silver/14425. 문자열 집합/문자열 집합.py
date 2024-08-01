n,m=map(int, input().split())
s=set(input() for _ in range(n))
c=list(input() for _ in range(m))
print(sum(1 if i in s else 0 for i in c))