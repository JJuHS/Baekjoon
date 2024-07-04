n = int(input())
ans = {
    1:(1, 0),
    2:(0, 2),
    3:(0, 3),
    4:(1, 3)
}

def prime(x):
    arr = [1] * x
    s = int(x ** 0.5)
    for i in range(2, s + 1):
        if arr[i]:
            for j in range(i, x, i):
                arr[j] = 0
            arr[i] = 1
    return arr.count(1)
if n <= 4:
    print(*ans[n])
else:
    cnt = prime(n+1) - 2
    print(1 + n - 2 * cnt, -1 + 2 * cnt)