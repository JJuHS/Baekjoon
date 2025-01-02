import sys;input = sys.stdin.readline

def sol(s):
    t_loc = []
    res = 0
    for i, c in enumerate(s):
        if c == 'T':
            t_loc.append(i)

    size = len(t_loc)
    if size % 2:
        print(-1)
        return 
    if not size:
        print(0)
        return 
    
    stack = []
    for i in range(size):
        if not stack:
            stack.append(i)
            continue
        
        j = stack[-1]
        if (t_loc[i] - t_loc[j]) % 2:
            res += (t_loc[i] - t_loc[j])
            stack.pop()
        else:
            stack.append(i)
    
    print(-1 if stack else res)
    

for _ in range(int(input())):
    _, S = input(), input().strip()
    sol(S)