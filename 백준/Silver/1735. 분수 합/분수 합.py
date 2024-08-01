import math
a,b=map(int,input().split())
c,d=map(int,input().split())
x=math.lcm(b,d)
y=a*x//b+c*x//d
print(y//math.gcd(x,y), x//math.gcd(x,y))