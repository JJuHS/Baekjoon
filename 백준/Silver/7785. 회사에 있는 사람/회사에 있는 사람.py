import sys;input=sys.stdin.readline
res=set()
for _ in range(int(input())):
    a,b=map(str,input().split())
    if b == 'enter':res.add(a)
    else:res.discard(a)
res=sorted(list(res),reverse=True)
for i in res:print(i)