import sys; input = sys.stdin.readline
from heapq import heappop, heappush

for tc in range(1, int(input()) + 1):
    up, down = [], []
    m = int(input())
    
    arr = []
    n = m
    while True:
        arr  = arr + list(map(int, input().split()))
        if n < 10:break
        n -= 10
        
    res = []
    
    for i in range(m):
        now = arr[i]
        if i % 2: 
            heappush(up, now)
            heappush(down, -heappop(up))
        else:   
            heappush(down, -now)
            now = -heappop(down)
            heappush(up, now)
            res.append(str(up[0]))
    
    print(len(res))
    while True:
        if len(res) < 10:
            print(' '.join(res))
            break
        else:
            print(' '.join(res[:10]))
            res = res[10:]