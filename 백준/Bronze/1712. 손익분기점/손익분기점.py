a,b,c=map(int,input().split())
print(int(a//(c-b) + 1) if c>b else -1)