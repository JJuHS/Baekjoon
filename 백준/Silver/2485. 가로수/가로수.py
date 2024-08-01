import math, sys;input=sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
s = [arr[i] - arr[i - 1]for i in range(1, n)]
a = math.gcd(*s)
print(sum([s[i] // a - 1 for i in range(n - 1)]))
