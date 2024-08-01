input()
a=set(map(int, input().split()))
input()
b=list(map(int, input().split()))
c=[1 if i in a else 0 for i in b]
print(*c)