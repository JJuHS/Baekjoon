div = 1000000007

n, k = map(int, input().split())

factorial = [1] * (n + 1)
for i in range(1, n + 1):factorial[i] = (factorial[i - 1] * i) % div

def square(x, y):
    if y <= 1:return [1, x][y]

    half = square(x, y//2)
    if y % 2:return half*half*x%div
    return half*half%div

print(factorial[n] * square(factorial[k]*factorial[n-k]%div ,div-2) % div)
