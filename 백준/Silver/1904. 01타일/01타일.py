n = int(input())
mod = 15746
if n < 4:
    print(n)
    exit()

res1 = 1
res2 = 2
res3 = 3

for i in range(4, n + 1):
    res1, res2, res3 = res2, res3, (res2 + res3) % mod

print(res3)