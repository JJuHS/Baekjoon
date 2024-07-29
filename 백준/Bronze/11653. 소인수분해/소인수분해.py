n = int(input())
for i in range(n):
    div = 2
    while n != 1:
        if n % div == 0:
            n //= div
            print(div)
        else:
            div += 1