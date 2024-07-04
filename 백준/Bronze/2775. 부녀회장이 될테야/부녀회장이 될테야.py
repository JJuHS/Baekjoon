t = int(input())

for _ in range(t):  
    k = int(input())
    n = int(input())
    a = [x for x in range(1, n+1)]
    for k in range(k):
        for i in range(1, n):
            a[i] += a[i-1]
    print(a[-1])