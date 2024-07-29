a=c=1e6
b=d=-1e6
for x, y in [list(map(int, input().split())) for _ in range(int(input()))]:
    a,b,c,d=min(a,x),max(b,x),min(c,y),max(d,y)
print((b-a)*(d-c))
