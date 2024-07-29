p = []
def sol(x):
    if x in p:
        return True
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    p.append(x)
    return True
m, n, res1, res2 = int(input()), int(input()), 0, 1e5

for i in range(m, n + 1):
    if sol(i):
        res1 += i
        res2 = min(res2, i)
if res1:
    print(res1)
    print(res2)
else:
    print(-1)