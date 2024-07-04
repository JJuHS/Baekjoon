N = int(input())
for i in range(1,N+1):
    a = ['*']*i
    b=''
    for j in range(len(a)):
        b += a[j]
        if j==len(a)-1:
            print(b.rjust(N))
    