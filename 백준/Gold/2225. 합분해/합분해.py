import math
n,k=map(int,input().split())
print(math.comb(n+k-1,k-1)%10**9)
