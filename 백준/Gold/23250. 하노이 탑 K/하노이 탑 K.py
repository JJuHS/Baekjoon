n, k = map(int, input().split())

def hanoi(x:int=n, now:int=k, a:int=1, b:int=3, c:int=2):
    if x == 1:
        if now == 1:
            print(a, b)
        return
    
    half = 2**(x - 1)
    if now < half:
        hanoi(x - 1, now, a, c, b)
    elif now == half:
        print(a, b)
    else:
        hanoi(x - 1, now - half, c, b, a)
    
hanoi()