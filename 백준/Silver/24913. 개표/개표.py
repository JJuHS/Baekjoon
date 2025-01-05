import sys;input = sys.stdin.readline

def sol1(x, p):
    candidates[p] += x
    return

def sol2(x, y):
    my = candidates[n] + x

    cnt = 0
    for i in range(n):
        if my > candidates[i]:
            cnt += my - candidates[i] - 1
        else: 
            print('NO')
            return
        
    print('YES') if cnt >= y else print('NO')

n, q = map(int, input().split())
candidates = [0] * (n + 1)

for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        sol1(b, c - 1) 
    else:
        sol2(b, c)
