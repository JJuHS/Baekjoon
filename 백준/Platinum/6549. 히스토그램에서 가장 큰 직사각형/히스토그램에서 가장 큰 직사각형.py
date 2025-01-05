import sys; input = sys.stdin.readline

while 1:
    n, *heights = map(int, input().split())
    if not n:break
    
    res = 0
    stack = []
    for i in range(n + 1):
        now = heights[i] if i != n else 0
        idx = None        
        while stack and stack[-1][0] >= now:
            h, idx = stack.pop()
            res = max(res, (i - idx) * h)

        stack.append((now, idx if idx is not None else i))

    print(res)