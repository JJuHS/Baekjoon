import sys
n, k = map(int, input().split())
coin = [int(sys.stdin.readline().strip()) for _ in range(n)]
ans = 0

for c in reversed(coin):
    ans += k // c
    k %= c
print(ans)
