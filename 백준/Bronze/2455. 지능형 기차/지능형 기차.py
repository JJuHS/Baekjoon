res,now=0,0
for _ in range(4):
    a,b=map(int,input().split())
    now+=b-a
    res=max(res,now)
print(res)