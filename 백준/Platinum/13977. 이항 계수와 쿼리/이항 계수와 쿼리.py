import sys
factorial = [1] * 4000001
for i in range(2, 4000001):
    factorial[i] = factorial[i - 1] * i % 1000000007


def find(x, n):
    if n == 1:
        return x % 1000000007
    else:
        tmp = find(x, n // 2)
        if n % 2 == 0:
            return tmp * tmp % 1000000007
        else:
            return tmp * tmp * x % 1000000007


m = int(sys.stdin.readline())
for _ in range(m):
    n, r = map(int, sys.stdin.readline().split())
    print(factorial[n] * find(factorial[r] * (factorial[n - r]), 1000000007 - 2) % 1000000007)