n, b = map(str, input().split())
res = 0
res, n, b = 0, list(n)[::-1], int(b)
for i in range(len(n)):
    if n[i].isalpha():res += (ord(n[i]) - 55) * b ** i
    else:res += int(n[i]) * b ** i
print(res)
