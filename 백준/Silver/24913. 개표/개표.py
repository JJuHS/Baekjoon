import sys;input = sys.stdin.readline

def sol(x, y):
    my = candidates[n] + x
    if my <= max_vote:
        print('NO')
        return
    cnt = n * (my - 1) - (total - candidates[-1])
        
    print('YES') if cnt >= y else print('NO')

n, q = map(int, input().split())
candidates = [0] * (n + 1)
total = 0
max_vote = 0

for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        total += b
        candidates[c-1] += b
        if c-1 != n and max_vote < candidates[c-1]:
            max_vote = candidates[c-1]
    else:
        sol(b, c)
